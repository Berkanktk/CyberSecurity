# Password security

When a password is hashed, a one-way hashing algorithm function is performed on a password that generates a fingerprint or representation of the provided password, which we then identify as the hash. One-way hashing functions are generally easy to compute. However, the computation required to obtain the original input (plaintext password in this case) could be difficult and time-consuming, depending on the algorithm.

We can make the distinction between two types of attacks against passwords, namely online and offline attacks.

**Online vs offline attacks:**

- In an online attack, password guessing can be largely defended against using some form of timeout between each entry or even some more extreme measure, by denying access to the account after an x number of attempts.
- In an offline setting, however, password guessing is much more accessible due to the dedicated hardware and advanced methods. This could be used by attackers that have obtained a database dump of usernames and passwords. Since the attack is carried out offline and without any intervention from the victim(s), this type of attack is almost impossible to defend against. However, this attack could be mitigated

# Password breaches

Such data breaches enable attackers to carry out offline attacks against a specific user or all users to find out their passwords.

## Passwords complexity

A brute-force attack grows exponentially with increasing key size

If the function was to be, f(x) = $3^x$, then it would require us triple the amount of work to go from $3^x$ to $3^x+1$ and so on. So if you were to have a password with a key size of a certain length, you could always calculate how long a brute-force attack will take against your password

## Statistics about passwords (length)

Based on personal information: You could make a password that is a combination of birthdates, names, residency, etc. This method is easy to guess for someone that knows this information, but more importantly, easy to brute-force as well

To give you an idea, how big this number is, there are about thirty-five trillion possible combinations using birthdays, place of birth/residence, common English names. While this might seem like a huge number, it is in fact almost nothing for what computers are capable of doing nowadays. This number varies based on the hash algorithm used (if any) to protect the passwords, but my 2017 laptop computes 223 MD5 hashes per second while some fancier cracking-stations even are able to compute 180 billion (237) MD5 hashes per second. Imagine what a nation-state is capable of.

- Based on 10-16 character words from the dictionary: The Oxford English dictionary has 218,632 (including obsolete words) < 2^18. This even includes words that are less than 10 characters in length which stands no chance against an offline attack.,
- Obfuscated words: The user picks a random 10-16 character word from a dictionary and applies some pseudo transformations (e.g. leetspeak). For example, dictionary -> d1c71on4ry. The Oxford English dictionary has 2^18 words * 2^12 (leetspeak extra chars) < 2^30. This does make your passwords harder to guess, but it is still in the danger zone when it comes to offline attacks.
- What about the Diceware method? Which is simply picking a number of words from a certain list of words. Say we have 7776 (= 6^5) words to choose from. Then choosing 3 words results in 7776^3 < 2^39 Which is quite small. 4 words are already better 7776^4 < 2^52 . 6 words is getting us somewhere 7776^6 < 2^78. This is however still easy to enumerate using words from the dictionary.
- Generating a password from a certain set of characters: Say a user generates a password randomly from the following set of characters: [a-zA-Z0-9.,;-+*/_=] (lower & upper case letters, numbers, and 9 special characters). The size of options we are choosing from is denoted as |S| = 26 + 26 +10 + 9 = 71. Then each character can be any of those 71 possible characters. So if we were to have a password of length 8, we would get 71^8 < 2^50. A password with 14 characters < 2^86 assuming each character is drawn uniformly at random.

What does it mean to have each character is drawn uniformly at random? It means that every character is just as likely to be chosen. So for example, the password 'aaaaaaaaaaaaaa', even though it is 14 characters long, it is not random and therefore the time 2^86 doesn't apply here.

What if we use some password-generating program like pwgen for Linux? Which is a program that "generates passwords which are designed to be easily memorized by humans, while being as secure as possible". `pwgen` has a flag `-s`, which stands for `-secure`. This is what the documentation says about the ease of remembering the generated passwords: "Generate completely random, hard-to-memorize passwords. These should only be used for machine passwords, since otherwise, it's almost guaranteed that users will simply write the password on a piece of paper taped to the monitor...".

The bottom line is, a secure password without any additional mechanisms to make it harder for attackers to crack, is simply out of reach. So websites and any platform that has a hold of your passwords, certainly need to hash your passwords, and even take additional measures such as using salt and algorithms designed specifically to make it harder to crack passwords.

# Password Attacks

No matter how complex a password is, how robust a hashing algorithm is, with unlimited (or at least sufficient) computing power or storage any password is breakable.

An attacker would most likely prefer to steal a password in transit form for unencrypted login pages, through keylogging, via phishing, etc. However, if that is not possible, the attacker could still get their hands on passwords using some of the various methods below.

**Guessing** 

Unlike software that is dedicated to producing pseudo-random passwords, human-generated passwords tend to not be all that random. Most often, passwords are related to the interests of a person, relatives, pets, dates, etc. All this information makes it easier for an attacker to gain the password without having to use any sophisticated attack. For instance, just by trying potential combinations such as name + birth date could produce results.

**Dictionary attack** 

This attack uses a simple file that could contain words, names, numbers, special characters, combinations or/and passwords from a past breach. One of the wordlists you are probably familiar with is the Rockyou wordlist. It is provided by Kali Linux in its standard installation and contains 14,341,564 unique passwords. Rockyou (The company) stored these password in plaintext for the attacker to see, download, and share :-)

**Rainbow tables**

Rainbow table attacks are a variant of dictionary attacks, in which pre-computed dictionaries are used to trade storage space for decreased time.  This method is particularly effective when an attacker tries to crack a large number of passwords. Although the pre-computation takes a considerable amount of time to generate the dictionary, the time to carry out the attack is faster as the generation is done before the attack is carried out.

**Brute-force attack** 

Unlike Dictionary attacks that use a predefined list of passwords, a brute-force attack extensively works through all possible combinations of letters a-zA-Z, number 0-9 and special characters that could make up a password. Depending on the password length, a brute-force attack may take a considerable amount of time or is just too impractical to carry out

Using passwords that are hard to guess and salting them while using strong hash functions are amongst the best precautions we could take as defenders.

# Password Storage and Defense Mechanisms

**Storing passwords in plain text:** The account database simply contains the login name and plaintext password of the users. This is the worst-case scenario! A password breach could be misused immediately by an attacker. Password reuse for other services is imminent and unfortunately is still a widespread issue!

**Storing hashed passwords**: Store the username and the derived key (hashed password) in a database: DK = hashFunction(Password). While this is better than storing passwords in plain text, it still has a lot of weaknesses. As the same password hashes to the same derived key. An attacker can pre-compute or download a large password/hash table and use it to look up passwords easily! For example, a password made from English words is 218 * 8Bytes ~ (~ means approximately) 2MB file. In other words, if an attacker were to compute a list of password hashes of each word in the English dictionary, this would result in a 2MB file and they just need to look up whether a certain password hash is in their list. 8 characters from [a-z] is 26^8 = 2^38 * 8 Bytes ~ 2.2 terabyte of pre-computation storage is needed for near-instant lookup. 10 characters [a-zA-Z] is 52^10 = 2^57 * 8Bytes ~ 1.6 exabyte ( 1 exabyte is equal to 1 million terabytes) of pre-computation storage is needed

This doesn't mean that that much storage is required to carry out such a big attack! This simply means, if an attacker wants to do a table lookup and not go through the hassle of brute-forcing 2^57 combinations, they would need this much storage. So at one end of the spectrum, you have using 0 storage and brute-forcing 2^57 possibilities and on the other end, you have using 1.6EB and having an almost instant lookup of the password. This means that an attacker can, for instance, have 0.8 EB (half of the 1.6EB) in storage and then do half of the brute-forcing work (half of 257). This is known as a time-space tradeoff. You could save time by using a lot of storage or you could save a lot of storage by brute-forcing.

**Salt**: Storing hashed passwords with salt increase the size of the possible passwords.. For each user, an individual random salt is generated and stored (plainly) along with the login name and password hash.Compute password hash as:

DK = hash(Salt || Password) or hash(Password || Salt ) (where || means concatenation)If the salt is long enough, the attacker can’t use pre-computed tables anymore. This certainly doesn't solve all the problems, but it slows down an (offline) attack significantly.

Calculate amount of storage to crack passwords almost instantly:

`numberOfCharactersInSet^numberOfCharacters * 8bytes`

i.e: A password that is made of 8 characters from [a-zA-Z] needs 52^8 * 8bytes of storage 

# Different Hashes Have Different Cracking Speeds

A collision is when two different values (i.e. passwords) result in the same hash. This speeds up the cracking time

- **Key separation**: This is a way to derive multiple independent passwords from a master password.
- **Key stretching**: This function essentially allows you to create a longer password using a short one, effectively, increasing the length of the password.
- **Key whitening**: Some algorithms (such as block ciphers) require the key to consist of some fixed amount of random bits. A key that is not in the desired format could still be transformed using a key whitening function.

## **Password-Based Key Derivation Function 2 (PBKDF2)**

In this case, the password is stored as follows: DK = PBKDF2(PRF, Password, Salt, c, dkLen) where PRF is a pseudorandom function (i.e. the hash function, such as HMAC) with output length hLen. Password is the master password. Salt is a sequence of bits, known as a cryptographic salt. c is the number of iterations desired (cost). dkLen is the desired length of the derived key. DK is the generated derived key. For example, WPA2 uses: DK = PBKDF2(HMAC−SHA1, password, ssid, 4096, 256).

Pros of PBKDF2:

The number of iterations could be adjusted which makes brute-forcing more difficult.

Cons of PBKDF2:

It uses a cryptographic hash function designed for speed, which is a con when you want to use this algorithm to slow attackers down.

It does not require much memory from the attacker.

It offers low protection against GPU/FPGA/ASIC based crackers.

## bcrypt

DK = bcrypt(Cost, Salt, Password) where Cost is a parameter to control the time cost. Salt is a sequence of bits, known as a cryptographic salt. Password is the master password. DK is the generated derived key. Bcrypt uses Blowfish encryption with a modified key setup function that was designed by Bruce Schneier (remember this name for later on). Blowfish is a symmetric-key block cipher that has a relatively large cost when it comes to changing keys. Each new key requires a relatively large pre-processing step, which makes Blowfish slow when it comes to changing keys. This is exactly why it is used in bcrypt.

Pros of bcrypt:

Has a cost factor to adapt to changes in computing power.

It uses an expensive function based on Blowfish encryption.

Cons of bcrypt:

It does not require much memory from the attacker.

It offers medium protection against GPU/FPGA/ASIC based crackers

## scrypt

scrypt can be seen as an updated version of bcrypt. DK = scrypt(Password,Salt,N,p,dkLen) where dkLen is the intended output length of the derived key. N is the CPU/memory cost parameter. p is the parallelization parameter (that multiplies the amount of work to be done so that the additional workloads are independent of each other and can be performed in parallel).

Pros of scrypt:

Has a cost factor for both time and memory.

It uses PBKDF2 as a building block.

Cons of scrypt:

The cost for both time and memory-bound to one parameter.

“Too new” compared to bcrypt; crypto ripens with age

## Argon2

Similar to bcrypt and scrypt, Argon2 also has a dkLen parameter. But it is different in the sense that it has different parameters for the CPU cost and memory cost. t is the CPU cost parameter and m is the memory cost parameter. It also has a parallelization parameter named p.

Pros of Argon2:

The cost for memory and time can be controlled separately.

Two versions, one with higher cost (cryptocurrencies), one secure against timing attacks (password hashing).

Argon2 was the winner of the Password Hashing Competition (PHC).

Cons of Argon2:

Even newer than scrypt!

## **Critique of such hashing functions**

While these hashing functions certainly offer great higher cost to the attacker to carry out their attack, compared to a more traditional like SHA-256, they also come at a cost for the platform. The mathematical operations required to compute the hash is also somewhat costly for the server. In other words, they require extensive computation to process a login event.

 

In fact, many big companies are using these functions already, such as Facebook that uses scrypt.

# Bruce Schneier Advices

Bruce Schneier, an American cryptographer that created the Blowfish cipher, suggests the following:

1. Never reuse a password you care about. Even if you choose a secure password, the site it’s for could leak it because of its own incompetence.You don’t want someone who gets your password for one application or site to be able to use it for another.
2. Don’t bother updating your password regularly. Sites that require 90-day – or whatever – password upgrades do more harm than good. Unless you think your password might be compromised, don’t change it.
3. Beware the “secret question”. You don’t want a backup system for when you forget your password to be easier to break than your password.Really, it’s smart to use a password manager. Or to write your passwords down on a piece of paper and secure that piece of paper.
4. One more piece of advice: if a site offers two-factor authentication, seriously consider using it. It’s almost certainly a security improvement.

Advice for administrators/developers (not from Bruce Schneier):

1. DO NOT STORE PLAINTEXT PASSWORDS!
2. The extra cost for strong password hashing is justified!