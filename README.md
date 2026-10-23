# OS Maker

A Python Tkinter app that generates a minimal x86 assembly bootloader project and a Windows 7-inspired desktop preview. This project is meant as a working starter kit for a simple OS mock-up and educational assembly project.

## What it generates

- `boot.asm` — a minimal NASM boot sector that prints a boot message and halts.
- `kernel.asm` — a simple 16-bit kernel stub that prints a welcome message.
- `desktop.py` — a Python Tkinter window styled to resemble Windows 7.
- `Makefile` — compiles the assembly files to binary output.
- `run_qemu.sh` — launches QEMU to boot the generated image.
- `README.md` — project usage notes.

## How to run

1. Open a terminal in the repo root.
2. Run:

```bash
python3 os_maker.py
```

3. Enter a project name and author.
4. Click Generate OS.
5. The app will create a new folder under `generated/`.
6. To build the boot sector:

```bash
cd generated/<project_name>
nasm -f bin -o boot.bin boot.asm
```

7. To boot it with QEMU:

```bash
qemu-system-i386 -drive file=boot.bin,format=raw,if=floppy
```

## Important note

This is a small, educational operating-system starter. It is not a full Windows 7 clone or a complete real OS. It demonstrates the boot process, assembly basics, and a graphical desktop mock-up inspired by Windows 7.
