import argparse
import csv
import os
import time

import torch
import torch.nn as nn


def make_data(n=4096, d=32, seed=0):
    g = torch.Generator().manual_seed(seed)
    X = torch.randn(n, d, generator=g)
    w = torch.randn(d, 1, generator=g)
    y = X @ w + 0.1 * torch.randn(n, 1, generator=g)
    return X, y


def save_ckpt(path, model, opt, step, epoch):
    """先写临时文件再原子替换，防止写到一半被杀导致损坏"""
    tmp = path + ".tmp"
    torch.save({
        "model": model.state_dict(),
        "optim": opt.state_dict(),
        "step": step,
        "epoch": epoch,
    }, tmp)
    os.replace(tmp, path)


def load_ckpt(path, model, opt):
    if not os.path.exists(path):
        return 0, 0
    ckpt = torch.load(path, map_location="cpu")
    model.load_state_dict(ckpt["model"])
    opt.load_state_dict(ckpt["optim"])
    return int(ckpt["step"]), int(ckpt["epoch"])


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--max-steps", type=int, default=200)
    p.add_argument("--save-every", type=int, default=20)
    p.add_argument("--batch-size", type=int, default=64)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--ckpt-dir", default="ckpt")
    p.add_argument("--log-dir", default="logs")
    args = p.parse_args()

    os.makedirs(args.ckpt_dir, exist_ok=True)
    os.makedirs(args.log_dir, exist_ok=True)

    ckpt_path = os.path.join(args.ckpt_dir, "last.pt")
    csv_path = os.path.join(args.log_dir, "metrics.csv")

    X, y = make_data()
    model = nn.Sequential(
        nn.Linear(32, 128), nn.ReLU(),
        nn.Linear(128, 1),
    )
    opt = torch.optim.Adam(model.parameters(), lr=args.lr)
    loss_fn = nn.MSELoss()

    start_step, epoch = load_ckpt(ckpt_path, model, opt)
    if start_step > 0:
        print(f"[resume] from step {start_step}")

    if not os.path.exists(csv_path):
        with open(csv_path, "w", newline="") as f:
            csv.writer(f).writerow(["step", "epoch", "loss", "lr", "elapsed"])

    t0 = time.time()
    step = start_step

    try:
        while step < args.max_steps:
            idx = torch.randint(0, len(X), (args.batch_size,))
            xb, yb = X[idx], y[idx]

            opt.zero_grad()
            loss = loss_fn(model(xb), yb)
            loss.backward()
            opt.step()

            step += 1
            epoch = step // max(1, len(X) // args.batch_size)

            if step % 5 == 0:
                with open(csv_path, "a", newline="") as f:
                    csv.writer(f).writerow([
                        step, epoch, f"{loss.item():.6f}",
                        f"{opt.param_groups[0]['lr']:.6f}",
                        f"{time.time() - t0:.2f}",
                    ])
                print(f"step {step:4d}  loss {loss.item():.6f}")

            if step % args.save_every == 0:
                save_ckpt(ckpt_path, model, opt, step, epoch)

    except KeyboardInterrupt:
        print("\n[interrupted] saving checkpoint ...")
        save_ckpt(ckpt_path, model, opt, step, epoch)
        print(f"saved at step {step}. run again to resume.")
    else:
        save_ckpt(ckpt_path, model, opt, step, epoch)
        print(f"done. final step: {step}")


if __name__ == "__main__":
    main()
