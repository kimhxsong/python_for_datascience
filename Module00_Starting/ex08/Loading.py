import shutil
import sys
import time


def ft_tqdm(lst):
    start_time = time.time()

    terminal_size = shutil.get_terminal_size((10, 0))
    columns = terminal_size.columns
    width = columns - 40 if columns > 50 else 10

    for index, current in enumerate(lst):
        yield current
        elapsed_time = time.time() - start_time
        progress_ratio = (current + 1) / len(lst)

        wbuffer = f"{progress_ratio * 100:3.0f}%|" \
                  f"{'█' * int(progress_ratio * width):{width}}| " \
                  f"{current + 1}/{len(lst)} " \
                  f"[{int(elapsed_time / 60):02d}:{int(elapsed_time % 60):02d}<00:00, " \
                  f"{index / elapsed_time:.2f}it/s]"
        sys.stderr.write("\r")
        sys.stderr.flush()
        sys.stderr.write(wbuffer)
        sys.stderr.flush()


if __name__ == "__main__":
    lst = range(3333)
    ret = 0
    for elem in ft_tqdm(lst):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)
