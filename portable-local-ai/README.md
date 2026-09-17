# Portable Local AI Environment (PLAE)

> **Status:** Working cross-platform portable AI environment. Windows and Tails launch methods are configured, with terminal inference working reliably on both platforms.

## Project Overview

The **Portable Local AI Environment (PLAE)** is a self-contained local-LLM setup stored on an external NVMe drive. The goal is to be able to carry the drive between compatible computers, connect it over USB, and run a local AI model without depending on a cloud service or reinstalling the environment on every machine.

The project combines portable storage, `llama.cpp`, quantized GGUF models, and platform-specific startup scripts for Windows and Linux/Tails.

PLAE was designed around three main ideas:

- **Portability** — the models, launchers, scripts, and supporting files live together on one external drive
- **Offline operation** — inference can run locally without requiring an internet connection
- **Cross-platform use** — the same model storage can be used from both Windows and Tails/Linux

## Hardware

- **256 GB NVMe SSD**
- Dual-ended USB enclosure
  - USB Type-A connector
  - USB Type-C connector
- Enclosure supports up to **10 Gbps** on compatible USB connections

Using a dual-ended enclosure makes the drive easier to move between older systems with USB-A and newer systems with USB-C without carrying a separate adapter.

## Storage Layout

The NVMe is formatted as **exFAT** so the same data partition can be accessed from both Windows and Linux/Tails.

Drive label:

```text
ai_data
```

The portable environment is organized around folders for models, scripts, and reference documents.

Example layout:

```text
ai_data/
├── Models/
├── Scripts/
├── Documents/
└── llama.cpp/
```

The exact internal layout may continue to change as the toolkit develops, but the goal is to keep everything required for inference on the external drive whenever practical.

## Software

The project uses:

- **llama.cpp** for local LLM inference
- **GGUF** quantized model files
- Windows batch scripts for Windows startup
- Bash scripts for Tails/Linux startup
- Tails as the portable Linux environment

The tested `llama.cpp` build used during setup was from the **b10516** generation.

## Current Model

The primary model configured for the environment is:

```text
Qwen3-4B-Q4_K_M.gguf
```

A Qwen3 4B Instruct variant was also tested during development.

The 4-bit quantized model was selected to keep memory and storage requirements practical while still providing a useful local assistant on ordinary hardware.

## Cross-Platform Design

```text
                     +---------------------+
                     |   256 GB NVMe SSD   |
                     |      ai_data        |
                     +----------+----------+
                                |
                  +-------------+-------------+
                  |                           |
             USB-A / USB-C               USB-A / USB-C
                  |                           |
          +-------+-------+           +-------+-------+
          |    Windows    |           | Tails / Linux |
          +-------+-------+           +-------+-------+
                  |                           |
             .bat launcher              Bash launcher
                  |                           |
                  +-------------+-------------+
                                |
                           llama.cpp
                                |
                         GGUF AI Model
                                |
                         Local Inference
```

The model file itself does not need to be duplicated for each operating system. Windows and Tails use different launch scripts but point to the same model stored on the NVMe.

## Windows Mode

A Windows batch launcher was created so the environment can be started without manually rebuilding the full command each time.

The Windows side of the project demonstrated:

- Running `llama.cpp` directly from portable storage
- Loading the GGUF model from the external NVMe
- Reusing a saved startup command through a `.bat` file
- Keeping model data separate from the host computer

This makes the environment much closer to a plug-in toolkit than a traditional locally installed AI application.

## Tails / Linux Mode

A Bash startup script was created for Tails so the same AI environment can be used from the live operating system.

Script location when the drive is mounted in Tails:

```text
/media/amnesia/ai_data/Scripts/Start-Qwen4B.sh
```

The script can be made executable with:

```bash
chmod +x /media/amnesia/ai_data/Scripts/Start-Qwen4B.sh
```

and launched with:

```bash
/media/amnesia/ai_data/Scripts/Start-Qwen4B.sh
```

I also created reference text files on the drive containing the commands needed to reach the document and script locations so the environment is easier to recover and use after booting a fresh Tails session.

## Tails Troubleshooting

One challenge during setup was browser/server-mode inference under Tails.

The `llama-server` process was tested with a local address using:

```text
127.0.0.1:8080
```

but the browser interface refused the connection even though command-line inference was functional.

Rather than treating the entire environment as broken, I isolated the issue to the server/browser path and kept the working terminal-based inference method as the reliable Tails workflow.

This was an important troubleshooting lesson: verify the underlying model and inference engine independently before assuming a UI or network-layer problem means the entire application stack has failed.

## Terminal-First Fallback

A major design benefit of PLAE is that it does not depend on a graphical interface.

If a web UI, local server, or browser integration fails, the model can still be used directly from the terminal through `llama.cpp`.

That makes the environment more resilient across different computers and operating systems.

## Why exFAT?

The portable AI drive needs to be readable and writable from both Windows and Linux environments.

Using exFAT allows the model files, scripts, and documents to remain on one shared storage volume rather than maintaining separate Windows and Linux copies.

This is especially useful for large GGUF model files that would otherwise waste significant storage if duplicated.

## Portability Goals

The finished workflow is intended to be:

```text
Connect NVMe
     |
Choose Windows or Tails/Linux launcher
     |
Load llama.cpp + model from ai_data
     |
Run AI locally
```

The host computer supplies the CPU and RAM, while the external drive carries the model and portable environment.

Actual inference performance therefore depends on the hardware of whichever computer the drive is connected to.

## What I Learned

This project provided hands-on experience with:

- Local LLM deployment
- `llama.cpp`
- GGUF model formats
- Quantized AI models
- Windows batch scripting
- Bash scripting
- Linux file permissions
- Cross-platform filesystem planning
- Portable software design
- External NVMe storage
- USB-A and USB-C compatibility
- Tails/Linux troubleshooting
- Localhost and application-server troubleshooting
- Designing graceful fallbacks when a preferred interface fails

## Security and Privacy Considerations

Because inference runs locally, prompts do not need to be sent to a remote AI service as part of the normal PLAE workflow.

The project is also designed so the AI files remain on the removable NVMe rather than being permanently installed on every host system.

Public documentation does not include credentials, personal documents, or other private files stored on the actual drive.

## Current Limitations

- Performance varies significantly depending on the host computer's CPU and available RAM
- The current environment is focused primarily on CPU inference
- Browser-based `llama-server` access did not work reliably under the tested Tails configuration
- The 256 GB drive places a practical limit on how many large models can be carried at once
- Platform-specific launch scripts still require separate maintenance

## Future Ideas

Possible future improvements include:

- Testing additional GGUF models while keeping the collection small and purposeful
- Improving automatic path detection between Windows and Linux
- Revisiting a lightweight browser interface for Tails
- Adding hardware-detection or memory checks before launching a model
- Creating a simple menu for choosing between installed models
- Further reducing manual setup after connecting the drive to a new computer

## Project Log

### September 2026 — Initial PLAE Build

- Set up a 256 GB NVMe in a dual-ended USB-A / USB-C enclosure
- Formatted the shared AI data drive as exFAT and labeled it `ai_data`
- Added Qwen3 4B GGUF models
- Configured `llama.cpp` for local inference
- Created a Windows batch launcher
- Created a Tails/Linux Bash startup script
- Confirmed terminal inference works under Tails
- Investigated a local `llama-server` / browser connection issue under Tails
- Kept terminal inference as the reliable fallback workflow
- Added reference text files with commonly needed startup paths and commands

---

**Project by Alexander Rodriquez**

This document will be updated as PLAE gains additional models, launch options, or cross-platform improvements.