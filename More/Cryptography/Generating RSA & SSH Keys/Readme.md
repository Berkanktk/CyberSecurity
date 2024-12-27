# RSA & SSH Key Management Guide

This guide provides step-by-step instructions for managing RSA keys using OpenSSL for encryption and decryption, as well as generating SSH keys for authentication.

## Table of Contents
1. [RSA Key Management with OpenSSL](#rsa-key-management-with-openssl)
   - [Create a Private Key](#create-a-private-key)
   - [Generate the Public Key](#generate-the-public-key)
   - [Encrypt Data](#encrypt-data)
   - [Decrypt Data](#decrypt-data)
2. [SSH Key Generation with OpenSSH](#ssh-key-generation-with-openssh)
   - [Generate SSH Keys](#generate-ssh-keys)
   - [Display the Public Key](#display-the-public-key)

## RSA Key Management with OpenSSL

### Create a Private Key
The following command generates a private RSA key and saves it as `private_key.pem`. Using the `-aes256` option will encrypt the key with a passphrase. To omit passphrase protection, remove the `-aes256` flag.
```bash
openssl genpkey -algorithm RSA -out private_key.pem -aes256
```

### Generate the Public Key
Using the generated private key, derive the corresponding public key and save it as `public_key.pem`:
```bash
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

### Encrypt Data
To encrypt a file (`data.txt`) using the public key, use:
```bash
openssl pkeyutl -encrypt -in data.txt -pubin -inkey public_key.pem -out encrypted_data.bin
```

### Decrypt Data
To decrypt the file (`encrypted_data.bin`), use the private key. If you used `-aes256` when creating the private key, you will be prompted for the passphrase.
```bash
openssl pkeyutl -decrypt -in encrypted_data.bin -inkey private_key.pem -out decrypted_data.txt
```

## SSH Key Generation with OpenSSH

### Generate SSH Keys
To create a new SSH key pair with RSA encryption and 4096 bits, run:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
This command will prompt you to set a filename (default is `~/.ssh/id_rsa`) and a passphrase for added security.

### Display the Public Key
To view and copy the generated public key:
```bash
cat ~/.ssh/id_rsa.pub
```
The public key can now be added to any server or service requiring SSH access.

## Notes
- **Passphrases**: Using a passphrase on your private keys adds a layer of security but requires you to enter the passphrase each time.
- **Key Security**: Always keep your private key secure. Never share it and ensure it is stored in a protected location.
