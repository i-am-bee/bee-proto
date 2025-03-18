> [!WARNING]  
 > 
 > This repository has been archived and is no longer actively maintained or updated. It is provided here for historical reference and may contain outdated or unsupported code. Users are encouraged to fork or adapt the contents as needed, but please note that no further updates, bug fixes, or security patches will be applied by the original maintainers.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="/docs/assets/Bee_logo_white.svg">
    <source media="(prefers-color-scheme: light)" srcset="/docs/assets/Bee_logo_black.svg">
    <img alt="Bee Framework logo" height="90">
  </picture>
</p>

<h1 align="center">bee-proto</h1>

<p align="center">
  <a aria-label="Join the community on GitHub" href="https://github.com/i-am-bee/bee-proto/discussions">
    <img alt="" src="https://img.shields.io/badge/Join%20the%20community-blueviolet.svg?style=for-the-badge&labelColor=000000&label=Bee">
  </a>
</p>

Protobuf interface and stubs for [Bee Agent Framework](https://github.com/i-am-bee/bee-agent-framework).

If you make changes to the proto files in `./proto`, you need to re-generate the `./gen` code. You need [Buf](https://buf.build/) for that (`brew install buf`).

1. Lint with: `buf lint proto`
2. Check breaking changes with: `buf breaking --against '.git#branch=main'`
3. Generate code with: `./scripts/generate.sh`


## Bugs

We are using [GitHub Issues](https://github.com/i-am-bee/bee-proto/issues) to manage our public bugs. We keep a close eye on this, so before filing a new issue, please check to ensure it hasn't already been logged.

## Code of conduct

This project and everyone participating in it are governed by the [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please read the [full text](./CODE_OF_CONDUCT.md) so that you can read which actions may or may not be tolerated.

## Legal notice

All content in these repositories including code has been provided by IBM under the associated open source software license and IBM is under no obligation to provide enhancements, updates, or support. IBM developers produced this code as an open source project (not as an IBM product), and IBM makes no assertions as to the level of quality nor security, and will not be maintaining this code going forward.
