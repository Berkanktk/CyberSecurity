# Key terms
`Version Disclosure` - vulnerability to find out the version of an application

| Term | Definition |
|:---:|:---:|
| Vulnerability | A vulnerability is defined as a weakness or flaw in the design, implementation or behaviours of a system or application. |
| Exploit | An exploit is something such as an action or behaviour that utilises a vulnerability on a system or application. |
| Proof of Concept (PoC) | A PoC is a technique or tool that often demonstrates the exploitation of a vulnerability. |

# Scoring vulnerabilities (CVSS & VPR)
Vulnerability scoring serves a vital role in vulnerability management and is used to determine the potential risk and impact a vulnerability may have on a network or computer system. 

Common Vulnerability Scoring System (CVSS) awards points to a vulnerability based upon its features, availability, and reproducibility.

## CVSS
A score is essentially determined by some of the following factors (but many more):
  1. How easy is it to exploit the vulnerability?
  2. Do exploits exist for this?
  3. How does this vulnerability interfere with the CIA triad?

I have put the Qualitative Severity Rating Scale and their score ranges into the table below. 
| Rating | Score |
|:---:|:---:|
| None | 0 |
| Low | 0.1 - 3.9 |
| Medium | 4.0 - 6.9 |
| High | 7.0 - 8.9 |
| Critical | 9.0 - 10.0 |

| Advantages of CVSS | Disadvantages of CVSS |
|:---:|:---:|
| CVSS has been around for a long time. | CVSS was never designed to help prioritise vulnerabilities, instead, just assign a value of severity. |
| CVSS is popular in organisations. | CVSS heavily assesses vulnerabilities on an exploit being available. However, only 20% of all vulnerabilities have an exploit available (Tenable., 2020) . |
| CVSS is a free framework to adopt and recommended by organisations such as NIST. | Vulnerabilities rarely change scoring after assessment despite the fact that new developments such as exploits may be found. |

## VPR
The VPR framework is a much more modern framework in vulnerability management. This framework is considered to be risk-driven; meaning that vulnerabilities are given a score with a heavy focus on the risk a vulnerability poses to the organisation itself, rather than factors such as impact (like with CVSS).

VPR is also considerably dynamic in its scoring, where the risk that a vulnerability may pose can change almost daily as it ages.

VPR uses a similar scoring range as CVSS, which I have also put into the table below. 
| Rating | Score |
|:---:|:---:|
| Low | 0.0 - 3.9 |
| Medium | 4.0 - 6.9 |
| High | 7.0 - 8.9 |

| Advantages of VPR | Disadvantages of VPR |
|:---:|:---:|
| VPR is a modern framework that is real-world. | VPR is not open-source like some other vulnerability management frameworks. |
| VPR considers over 150 factors when calculating risk. | VPR can only be adopted apart of a commercial platform. |
| VPR is risk-driven and used by organisations to help prioritise patching vulnerabilities. | VPR does not consider the CIA triad to the extent that CVSS does; meaning that risk to the confidentiality, integrity and availability of data does not play a large factor in scoring vulnerabilities when using VPR. |
| Scorings are not final and are very dynamic, meaning the priority a vulnerability should be given can change as the vulnerability ages. |  |

# CVE
In cybersecurity, vulnerabilities are classified under “Common Vulnerabilities and Exposures” (Or CVE for short).

These CVEs have the formatting of CVE-YEAR-IDNUMBER. For example, the vulnerability that the famous malware WannaCry used was CVE-2017-0144.

