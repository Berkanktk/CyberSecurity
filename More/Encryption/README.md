# Encryption 

## Symmetric vs Assymetric
### Symmetric
Symmetric encryption is where there is only one key in use. It might have to be encoded slightly differently for encryption or decryption, but it will be the same base nonetheless. With a symmetric encryption algorithm, Alice and Bob would have had to get together beforehand to share the key with each other.

### Asymmetric Encryption
Calling an encryption algorithm asymmetric is just a fancy way of saying that you need two different keys: one to encrypt, and one to decrypt. The public key is distributed to anyone who wants it, but the private key is kept only by the owner

| Asymmetric Encryption: | Symmetric Encryption: |
|---|---|
| Uses two keys: a public key for encryption and a private key for decryption | Uses one key to both encrypt and decrypt data. |
| Public key is distributed for anyone to use, private key must be kept a secret | The sole key must be kept hidden by both parties as it can be used to decode any communications if it’s intercepted |
| All communications are encrypted from the very beginning of the conversation — no “secret” exchange has to take place in order to securely send information. | Either the key must be sent insecurely across a network, or the people/computers involved must have a secret meeting to share the key before encrypted conversation can take place. |
| More difficult to use in three-way communication. | Can easily be used by many different people to send and read messages as a group. |

## RSA ENCRYPTION
RSA (short for Rivest–Shamir–Adleman — named after its creators) is an asymmetric public-key encryption system that is very commonly used in real world applications. 

Read more about RSA Encryption and the math behind [here](https://muirlandoracle.co.uk/2020/01/29/rsa-encryption/).

## How does HTTPS actually work?
HTTPS takes the well-known and understood HTTP protocol, and simply layers a SSL/TLS (hereafter referred to simply as “SSL”) encryption layer on top of it. Servers and clients still speak exactly the same HTTP to each other, but over a secure SSL connection that encrypts and decrypts their requests and responses. The SSL layer has 2 main purposes:

Verifying that you are talking directly to the server that you think you are talking to
Ensuring that only the server can read what you send it and only you can read what it sends back.

### How an SSL connection is established
An SSL connection between a client and server is set up by a handshake, the goals of which are:

To satisfy the client that it is talking to the right server (and optionally visa versa)
For the parties to have agreed on a “cipher suite”, which includes which encryption algorithm they will use to exchange data
For the parties to have agreed on any necessary keys for this algorithm

Read more about HTTPS [here](https://robertheaton.com/2014/03/27/how-does-https-actually-work/).

## What's a Digital Signature?
Digital signatures are a way to prove the authenticity of files, to prove who created or modified them. Using asymmetric cryptography, you produce a signature with your private key and it can be verified using your public key

## Certificates 
Certificates are also a key use of public key cryptography, linked to digital signatures.The certificates have a chain of trust, starting with a root CA (certificate authority). Root CAs are automatically trusted by your device, OS, or browser from install. Certs below that are trusted because the Root CAs say they trust that organisation. Certificates below that are trusted because the organisation is trusted by the Root CA and so on 

## Diffie Hellman Key Exchange
### What is Key Exchange?
Key exchange allows 2 people/parties to establish a set of common cryptographic keys without an observer being able to get these keys. Generally, to establish common symmetric keys.

### How does Diffie Hellman Key Exchange work?
Alice and Bob want to talk securely. They want to establish a common key, so they can use symmetric cryptography, but they don’t want to use key exchange with asymmetric cryptography. This is where DH Key Exchange comes in.

Alice and Bob both have secrets that they generate, let’s call these A and B. They also have some common material that’s public, let’s call this C.

We need to make some assumptions. Firstly, whenever we combine secrets/material it’s impossible or very very difficult to separate. Secondly, the order that they're combined in doesn’t matter.

Alice and Bob will combine their secrets with the common material, and form AC and BC. They will then send these to each other, and combine that with their secrets to form two identical keys, both ABC. Now they can use this key to communicate.

This is also visualized [here](https://www.youtube.com/watch?v=NmM9HA2MQGI).

## SSH Authentication
By default, SSH is authenticated using usernames and passwords in the same way that you would log in to the physical machine.

This uses public and private keys to prove that the client is a valid and authorised user on the server. By default, SSH keys are RSA keys. You can choose which algorithm to generate, and/or add a passphrase to encrypt the SSH key. `ssh-keygen` is the program used to generate pairs of keys most of the time.

### SSH Private Keys
You should treat your private SSH keys like passwords. **Don’t share them**, they’re called private keys for a reason. If someone has your private key, they can use it to log in to servers that will accept it unless the key is encrypted.

It’s very important to mention that the passphrase to decrypt the key isn’t used to identify you to the server at all, all it does is decrypt the SSH key. The passphrase is never transmitted, and never leaves your system.

Using tools like John the Ripper, you can attack an encrypted SSH key to attempt to find the passphrase, which highlights the importance of using a secure passphrase and keeping your private key private.

When generating an SSH key to log in to a remote machine, you should generate the keys on your machine and then copy the public key over as this means the private key never exists on the target machine.

### How do you use these keys?
The `~/.ssh` folder is the default place to store these keys for OpenSSH. The `authorized_keys` file in this directory holds public keys that are allowed to access the server if key authentication is enabled. By default on many distros, key authentication is enabled as it is more secure than using a password to authenticate. Normally for the root user, only key authentication is enabled.

In order to use a private SSH key, the permissions must be set up correctly otherwise your SSH client will ignore the file with a warning. Only the owner should be able to read or write to the private key (600 or stricter). `ssh -i keyNameGoesHere user@host` is how you specify a key for the standard Linux OpenSSH client.

Using SSH keys to get a better shell
SSH keys are an excellent way to “upgrade” a reverse shell, assuming the user has login enabled (www-data normally does not, but regular users and root will). Leaving an SSH key in authorized_keys on a box can be a **useful backdoor**, and you don't need to deal with any of the issues of unstabilised reverse shells like Control-C or lack of tab completion.

## PGP, GPG and AES
### What is PGP?
PGP stands for Pretty Good Privacy. It’s a software that implements encryption for encrypting files, performing digital signing and more.

### What is GPG?
GnuPG or GPG is an Open Source implementation of PGP from the GNU project. You may need to use GPG to decrypt files in CTFs. With PGP/GPG, private keys can be protected with passphrases in a similar way to SSH private keys. If the key is passphrase protected, you can attempt to crack this passphrase using John The Ripper and gpg2john. The key provided in this task is not protected with a passphrase.

## What about AES?
AES, sometimes called Rijndael after its creators, stands for Advanced Encryption Standard. It was a replacement for DES which had short keys and other cryptographic flaws.

AES and DES both operate on blocks of data (a block is a fixed size series of bits).

## The Future - Quantum Computers and Encryption
### Asymmetric and Quantum
While it’s unlikely we’ll have sufficiently powerful quantum computers until around 2030, once these exist encryption that uses RSA or Elliptical Curve Cryptography will be very fast to break. This is because quantum computers can very efficiently solve the mathematical problems that these algorithms rely on for their strength.

### AES/DES and Quantum
AES with 128 bit keys is also likely to be broken by quantum computers in the near future, but 256 bit AES can’t be broken as easily. Triple DES is also vulnerable to attacks from quantum computers.

### Current Recommendations
The NSA recommends using RSA-3072 or better for asymmetric encryption and AES-256 or better for symmetric encryption. There are several competitions currently running for quantum safe cryptographic algorithms, and it’s likely that we will have a new encryption standard before quantum computers become a threat to RSA and AES.