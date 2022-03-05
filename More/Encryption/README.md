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