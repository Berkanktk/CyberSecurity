# John The Ripper
John the Ripper is one of the most well known, well-loved and versatile hash cracking tools out there. It combines a fast cracking speed, with an extraordinary range of compatible hash types.

# Hashes
Hashes are fixed-length representations of data obtained through hashing algorithms. Popular hashing algorithms include MD4, MD5, SHA1, and NTLM.

## Why are Hashes Secure?
Hashing algorithms are designed to be one-way functions, making it computationally infeasible to reverse a hash and obtain the original data. This property is related to the P vs NP problem in mathematics.

## Cracking Hashes with John the Ripper
While hashes are not easily reversible, they can be cracked using methods like dictionary attacks. John the Ripper is a tool used for fast brute force attacks on various hash types, allowing attackers to discover the original data corresponding to a hash.

# Setting Up John The Ripper
To download John the Ripper for different operating systems, you can follow these steps:

<details> <summary>Linux and Unix-based Systems</summary>

   - **Debian/Ubuntu**: You can use the `apt` package manager to install John the Ripper:
     ```bash
     sudo apt-get install john
     ```

   - **Red Hat/CentOS/Fedora**: Use `yum` or `dnf` to install John:
     ```bash
     sudo yum install john
     ```

   - **Other Linux Distributions**: John the Ripper may be available in your distribution's package manager. Use the appropriate package manager command to install it.

</details>

<details> <summary>MacOS</summary>

   - You can use the popular package manager Homebrew to install John the Ripper on macOS. First, install Homebrew if you haven't already:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

   - Once Homebrew is installed, you can install John with the following command:
     ```bash
     brew install john-jumbo
     ```

</details>

<details> <summary>Windows</summary>

   - For Windows, you can download pre-built binaries of John the Ripper from the official website. Visit the following URL: https://www.openwall.com/john/ (Make sure to check for the latest version on the official website.)
  
   - Extract the downloaded ZIP file to a directory of your choice.
  
   - You can then use John the Ripper from the command prompt in the extracted directory.

</details>

<details> <summary>Other Operating Systems</summary>

* John the Ripper also supports various other operating systems. You can check the official John the Ripper website for downloads and installation instructions specific to your OS: https://www.openwall.com/john/

</details>


# Wordlists
**Wordlists**
To perform dictionary attacks on hashes, you need a wordlist—a list of words to hash and compare. You can find a variety of wordlists in the [SecLists](https://github.com/danielmiessler/SecLists) repository.

**Location:**
- On Parrot OS & Kali Linux you can access wordlists in the `/usr/share/wordlists directory`.

**Using RockYou:**
- RockYou is a popular wordlist that is used in many CTFs and password cracking tools. It is available in the `/usr/share/wordlists` directory on Parrot OS and Kali Linux.
- If you're not using the mentioned distributions, you can get rockyou.txt from the SecLists repository under `/Passwords/Leaked-Databases`. Extract it from .tar.gz format using `tar xvzf rockyou.txt.tar.gz`.

# Using John The Ripper

**List of Contents:**
- [Basic Syntax](#basic-syntax)
- [Automatic Cracking](#automatic-cracking)
- [Identifying Hashes](#identifying-hashes)
- [Format-Specific Cracking](#format-specific-cracking)
- [Cracking Windows Authentication Hashes](#cracking-windows-authentication-hashes)
- [Cracking /etc/shadow Hashes](#cracking-etcshadow-hashes)
- [Single Crack Mode](#single-crack-mode)
- [Custom Rules](#custom-rules)
- [Cracking Password Protected Zip Files](#cracking-password-protected-zip-files)
- [Cracking Password Protected RAR Archives](#cracking-password-protected-rar-archives)
- [Cracking SSH Keys with John](#cracking-ssh-keys-with-john)

## Basic Syntax
To use John the Ripper, you need to specify the hash type and the wordlist you want to use. The basic syntax is as follows:
```bash
john [options] [path to file]
```
* [path to file] - The file containing the hash you're trying to crack.

## Automatic Cracking
John has built-in features to detect what type of hash it's being given, and to select appropriate rules and formats to crack it for you, this isn't always the best idea as it can be unreliable- but if you can't identify what hash type you're working with and just want to try cracking it, it can be a good option! To do this we use the following syntax:

```bash
john --wordlist=[path to wordlist] [path to file]
```

* `--wordlist=` - Specifies using wordlist mode, reading from the file that you supply in the following path...

**Example Usage:**
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt
```

## Identifying Hashes
If John the Ripper doesn't automatically recognize and load hashes, you can use other tools to identify the hash type and then set John to use a specific format. Here are some methods:

1. Online Hash Identifiers: You can use online tools like [this](https://hashes.com/en/tools/hash_identifier) one to identify hash types by pasting the hash and getting the result.

2. Using `hash-identifier` Tool:
   * You can use a Python tool called `hash-identifier` to easily identify hash types.
   Download the tool using: wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py
   * Launch it with: python3 hash-id.py
   * Enter the hash you want to identify, and the tool will provide possible hash formats.

## Format-Specific Cracking
Once you have identified the hash type you're dealing with, you can instruct John the Ripper to use a specific format when cracking the hash. Use the following syntax:

```bash
john --format=[format] --wordlist=[path to wordlist] [path to file]
```

- `--format=`: This flag informs John that you're providing a hash in a specific format and to use that format for cracking.
- `[format]`: Replace this with the identified hash format.

**Example Usage:**
```bash
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt
```

**A Note on Formats:**
- For standard hash types like MD5, you may need to prefix them with `raw-` to indicate that it's a standard hash type. However, this isn't always necessary.
- To check if you need the prefix or not, you can list all of John's formats using `john --list=formats`. You can manually check or use `grep` to find your hash type, like `john --list=formats | grep -iF "md5"`.

## Cracking Windows Authentication Hashes
Now, let's dive into cracking something more challenging: Windows authentication hashes. These hashes are the hashed versions of passwords stored by Windows operating systems. To obtain these hashes, you often need to be a privileged user. 

**NTHash / NTLM:**
- NThash is the hash format used by modern Windows Operating Systems to store user and service passwords. It's also commonly referred to as "NTLM," which references the previous version of Windows password hashing known as "LM" (Lan Manager), hence "NT/LM."
- Historically, the "NT" designation in Windows products stood for "New Technology" and was used to differentiate products not built on the MS-DOS operating system. Eventually, the "NT" line became the standard for Microsoft's operating systems.
- You can acquire NTHash/NTLM hashes by dumping the Security Account Manager (SAM) database on a Windows machine using tools like Mimikatz or by extracting them from the Active Directory database (NTDS.dit).
- Cracking the hash is sometimes necessary, especially when there is a weak password policy in place. However, in some cases, you may not need to crack the hash and can conduct a "pass the hash" attack instead, which involves using the hash directly for authentication.

## Cracking /etc/shadow Hashes
The `/etc/shadow` file on Linux machines stores password hashes and related information for user accounts. To crack these hashes, you need sufficient privileges to access this file. Here's how to do it:

**Unshadowing:**
- John the Ripper requires a specific format to work with `/etc/shadow` passwords, so you need to combine it with the `/etc/passwd` file using the `unshadow` tool.
- The syntax for unshadow is as follows:
  ```
  unshadow [path to passwd] [path to shadow]
  ```
  - `unshadow` invokes the unshadow tool.
  - `[path to passwd]` is the path to a copy of the `/etc/passwd` file you've taken from the target machine.
  - `[path to shadow]` is the path to a copy of the `/etc/shadow` file you've taken from the target machine.
- Example usage:
  ```
  unshadow local_passwd local_shadow > unshadowed.txt
  ```
  - In this example, `local_passwd` contains the `/etc/passwd` line for the root user, and `local_shadow` contains the `/etc/shadow` line for the root user.

**Cracking:**
- After unshadowing, you can feed the output file (in this example, `unshadowed.txt`) directly into John the Ripper.
- In most cases, you won't need to specify a format, as the input is prepared specifically for John. However, if needed, you can specify the format using `--format=` (e.g., `--format=sha512crypt`).
- Example cracking command:
  ```
  john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt
  ```

## Single Crack Mode
**Single Crack Mode**

John the Ripper has another mode called Single Crack mode, which relies solely on the username to attempt to generate possible passwords heuristically. It does this by slightly altering the letters and numbers contained within the username to create variations.

**Word Mangling:**
- Single Crack mode uses word mangling, which means it generates possible passwords based on the username.
- For example, if the username is "Markus," some possible passwords could be "Markus1," "Markus2," "Markus3," and so on, as well as variations in capitalization and special characters like "MArkus," "MARkus," "MARKus," and "Markus!", "Markus$", "Markus*."
- John builds its own dictionary using a set of rules called "mangling rules" to mutate the username and generate a wordlist. This exploits the tendency of users to create poor passwords based on information about their username or the service they're logging into.

**GECOS:**
- John's word mangling implementation also works with the Gecos fields of UNIX-like operating systems such as Linux.
- The Gecos fields are the fields separated by colons (":") in records like `/etc/passwd` and `/etc/shadow`. These fields can include information like the user's full name and home directory.
- John can use this Gecos information to add to the wordlist it generates when cracking `/etc/shadow` hashes with Single Crack mode.

**Using Single Crack Mode:**
- To use Single Crack mode, you can use a syntax similar to what we've used before. For example, to crack the password of the user "Mike" using Single Crack mode, you'd use:
  ```bash
  john --single --format=[format] [path to file]
  ```
  - `--single`: This flag tells John to use the Single Crack mode.
  - `[format]`: Specify the hash format.
- Example usage:
  ```bash
  john --single --format=raw-sha256 hashes.txt
  ```

**A Note on File Formats in Single Crack Mode:**
- When using Single Crack mode, you need to change the file format you're feeding to John for it to understand what data to create a wordlist from.
- You do this by prepending the hash with the username that the hash belongs to. For example, change the file "hashes.txt" 
  
  from:  

  ```
  1efee03cdcb96d90ad48ccc7b8666033
  ```
  to:
  ```
  mike:1efee03cdcb96d90ad48ccc7b8666033
  ```
This way, John knows which username to base its word mangling on.

## Custom Rules
Custom rules in John the Ripper allow you to define your own sets of rules for generating passwords dynamically during the cracking process. This is especially useful when you have insights into the password structure or patterns used by your target.

**Common Custom Rules:**
- Organizations often require password complexity, such as having at least one capital letter, number, or symbol. Users tend to follow predictable patterns, like placing a capital letter first, followed by a number and then a symbol, to meet these requirements. Custom rules can exploit this predictability to generate passwords from wordlists.

**Creating Custom Rules:**
- Custom rules are defined in the `john.conf` file, usually located in `/etc/john/john.conf` (on Linux) or `/opt/john/john.conf`.
- Here's the syntax for creating custom rules:

```plaintext
[List.Rules:YourRuleName]
RegexPattern = "Modifier1 Modifier2 ..."
```

- `YourRuleName` is the name you give to your custom rule, which you'll use as an argument when running John.
- `RegexPattern` defines the pattern you want to apply to words in your wordlist.
- Modifiers like `Az` (append), `A0` (prepend), and `c` (capitalize) can be used in combination to specify where and how the word should be modified.
- Wiki for [Wordlist rules syntax ](https://www.openwall.com/john/doc/RULES.shtml)

**Common Modifier Examples:**
- `[0-9]`: Include numbers 0-9.
- `[0]`: Include only the number 0.
- `[A-z]`: Include both upper and lowercase letters.
- `[A-Z]`: Include only uppercase letters.
- `[a-z]`: Include only lowercase letters.
- `[a]`: Include only the letter 'a'.
- `[!£$%@]`: Include the symbols !£$%@.

**Example Custom Rule for "Polopassword1!":**

To generate passwords like "Polopassword1!" from the word "polopassword" in your wordlist, create a custom rule like this:

```plaintext
[List.Rules:PoloPassword]
cAz"[0-9] [!£$%@]"
```

- `c`: Capitalize the first letter.
- `Az`: Append to the end.
- `[0-9]`: Include a number from 0 to 9.
- `[!£$%@]`: Include one of the symbols !£$%@.

**Using Custom Rules:**
- To use a custom rule, you can provide it as an argument to John using the `--rule` flag.
- Example command:
  ```
  john --wordlist=[path to wordlist] --rule=PoloPassword [path to file]
  ```

If you find it challenging to write custom rules, Jumbo John already comes with a large list of custom rules that cover most cases. You can explore these rules in the `john.conf` file, usually around line 678, if your custom rule syntax isn't working correctly.

## Cracking Password Protected Zip Files
You can use John the Ripper to crack the password of a password-protected ZIP file. To do this, you'll need to use the `zip2john` tool to convert the ZIP file into a format that John can understand. Here's how you can use it:

**Using Zip2John:**
- The basic syntax for `zip2john` is as follows:
  ```
  zip2john [options] [zip file] > [output file]
  ```
  - `[options]`: Allows you to specify checksum options, which are often not necessary.
  - `[zip file]`: The path to the ZIP file you want to get the hash from.
  - `>`: Redirects the output to a file.
  - `[output file]`: The file where the hash will be stored.

**Example Usage:**
```bash
zip2john zipfile.zip > zip_hash.txt
```

After running `zip2john`, you will have a file (`zip_hash.txt`) containing the hash of the password-protected ZIP file.

Once you have the hash, you can use John the Ripper to attempt to crack the password using the same syntax you're familiar with:

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt
```

Replace `[path to zip_hash.txt]` with the actual path to your `zip_hash.txt` file. John will attempt to crack the ZIP file's password based on the provided hash.

## Cracking Password Protected RAR Archives
Just like with ZIP files, you can use John the Ripper to crack the password of a password-protected RAR archive. To do this, you'll need to use the `rar2john` tool to convert the RAR file into a hash format that John can understand. Here's how you can do it:

**Using Rar2John:**
- The basic syntax for `rar2john` is as follows:
  ```
  rar2john [rar file] > [output file]
  ```
  - `[rar file]`: The path to the RAR file you want to get the hash from.
  - `>`: Redirects the output to a file.
  - `[output file]`: The file where the hash will be stored.

**Example Usage:**
```shell
rar2john rarfile.rar > rar_hash.txt
```

After running `rar2john`, you will have a file (`rar_hash.txt`) containing the hash of the password-protected RAR archive.

Now, similar to the previous tasks, you can use John the Ripper to attempt to crack the RAR archive's password using the following syntax:

```shell
john --wordlist=[path to wordlist] rar_hash.txt
```

Replace `[path to wordlist]` with the actual path to your wordlist (e.g., `/usr/share/wordlists/rockyou.txt`). John will use the wordlist to try to crack the RAR archive's password based on the provided hash.

## Cracking SSH Keys with John
Certainly, you can use John the Ripper to crack the password of an SSH private key (`id_rsa`) file. When you use SSH key-based authentication, your private key file may be protected with a password. Here's how you can crack it using John the Ripper:

**Using SSH2John:**
1. First, you'll need to convert the `id_rsa` private key into a hash format that John can work with. You can do this with the `ssh2john` tool.

**Basic Syntax:**
   ```shell
   ssh2john [id_rsa private key file] > [output file]
   ```

   - `[id_rsa private key file]`: The path to the `id_rsa` private key file you want to get the hash from.
   - `>`: Redirects the output to a file.
   - `[output file]`: The file where the hash will be stored.

**Example Usage:**
   ```shell
   ssh2john id_rsa > id_rsa_hash.txt
   ```

After running `ssh2john`, you will have a file (`id_rsa_hash.txt`) containing the hash of the SSH private key.

**Cracking with John:**
2. Now, you can use John the Ripper to attempt to crack the SSH key password using the following syntax:

**Basic Syntax:**
   ```shell
   john --wordlist=[path to wordlist] id_rsa_hash.txt
   ```

   - `[path to wordlist]`: Replace this with the actual path to your wordlist (e.g., `/usr/share/wordlists/rockyou.txt`).
   - `id_rsa_hash.txt`: The file containing the hash of the SSH private key.

**Example Usage:**
   ```shell
   john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt
   ```

John will use the wordlist to try to crack the password of the SSH private key based on the provided hash.
