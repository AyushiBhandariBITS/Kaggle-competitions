import json
import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
import matplotlib.gridspec as gridspec

# === Define color palette ===
colors = [
    (0, 0, 0),        # 0 = black
    (30, 147, 255),   # 1 = blue
    (250, 61, 49),    # 2 = red
    (78, 204, 48),    # 3 = green
    (255, 221, 0),    # 4 = yellow
    (153, 153, 153),  # 5 = gray
    (229, 59, 163),   # 6 = pink
    (255, 133, 28),   # 7 = orange
    (136, 216, 241),  # 8 = light blue
    (147, 17, 49),    # 9 = dark red
]

def render_grid(ax, grid, title=""):
    """Convert numeric grid → color image on given axis"""
    img = [[colors[cell] for cell in row] for row in grid]
    ax.imshow(np.array(img))
    ax.set_title(title)
    ax.axis("off")

def count_colors(grid):
    """Count number of cells per color ID in a grid"""
    flat = [cell for row in grid for cell in row]
    return Counter(flat)

def find_differences(input_grid, output_grid):
    """Find coordinates where input and output differ"""
    diffs = []
    h = min(len(input_grid), len(output_grid))
    w = min(len(input_grid[0]), len(output_grid[0]))
    for i in range(h):
        for j in range(w):
            if input_grid[i][j] != output_grid[i][j]:
                diffs.append((i, j, input_grid[i][j], output_grid[i][j]))
    return diffs

def visualize_task(task_file, task_num):
    """Visualize all train/test grids from a JSON task file and save analysis in PNGs"""
    with open(task_file, "r") as f:
        task = json.load(f)

    # Create output dir for this task
    out_dir = f"Done/task_{task_num}_viz"
    os.makedirs(out_dir, exist_ok=True)

    # Loop over all sections: train, test, etc.
    for section in task.keys():
        for idx, example in enumerate(task[section]):
            # Use GridSpec: 2 rows (top: grids, bottom: text)
            fig = plt.figure(figsize=(10, 6))
            gs = gridspec.GridSpec(2, 2 if "output" in example else 1, height_ratios=[4, 1])

            # Top row: grids
            ax1 = fig.add_subplot(gs[0, 0])
            render_grid(ax1, example["input"], title=f"{section} {idx} - Input")

            if "output" in example:
                ax2 = fig.add_subplot(gs[0, 1])
                render_grid(ax2, example["output"], title=f"{section} {idx} - Output")

                # --- Analysis ---
                in_h, in_w = len(example["input"]), len(example["input"][0])
                out_h, out_w = len(example["output"]), len(example["output"][0])
                in_counts = count_colors(example["input"])
                out_counts = count_colors(example["output"])
                diffs = find_differences(example["input"], example["output"])

                info_text = (
                    f"Input size: {in_h}x{in_w} | Output size: {out_h}x{out_w}\n"
                    f"Input counts: {dict(in_counts)} | Output counts: {dict(out_counts)}\n"
                    f"Differences (i,j,in,out): {diffs if diffs else 'None'}"
                )

                # Bottom row: span full width
                ax_info = fig.add_subplot(gs[1, :])
                ax_info.axis("off")
                ax_info.text(0, 0.5, info_text, ha="left", va="center", fontsize=9, wrap=True)

            else:  # test examples only have input
                in_h, in_w = len(example["input"]), len(example["input"][0])
                in_counts = count_colors(example["input"])
                info_text = (
                    f"Input size: {in_h}x{in_w}\n"
                    f"Input counts: {dict(in_counts)}\n"
                    f"Output not available"
                )

                ax_info = fig.add_subplot(gs[1, :])
                ax_info.axis("off")
                ax_info.text(0, 0.5, info_text, ha="left", va="center", fontsize=9, wrap=True)

            # Save visualization to file
            out_path = os.path.join(out_dir, f"{section}_{idx}.png")
            plt.tight_layout()
            plt.savefig(out_path, dpi=150)
            plt.close(fig)

            print(f"Saved visualization → {out_path}")

visualize_task(f"task203.json", task_num=203)
