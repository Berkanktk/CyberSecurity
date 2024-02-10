# Active Directory

Active Directory (AD) is a system mainly used by businesses in Windows environments. It's a centralised authentication system. The Domain Controller (DC) is at the heart of AD and typically manages data storage, authentication, and authorisation within a domain.

You can think of AD as a digital database containing objects like users, groups, and computers, each with specific attributes and permissions. Ideally, it applies the principle of least privilege and uses a hierarchical approach to managing roles and giving authenticated users access to all non-sensitive data throughout the system. For this reason, assigning permissions to users must be approached cautiously, as it can potentially compromise the entire Active Directory. We'll delve into this in the upcoming exploitation section.

## Enumeration

Enumerating the Active Directory for the vulnerable permission is the first step to check if the current user has any write capabilities over another user on the AD.

1. `cd C:\Users\hr\Desktop` moves to the folder containing all the exploitation tools.
2. `powershell -ep bypass` will bypass the default policy for arbitrary PowerShell script execution.
3. `. .\PowerView.ps1` loads the PowerView script into the memory.

At this point, we can enumerate the privileges by running:

`Find-InterestingDomainAcl -ResolveGuids`

As you may see, this command will return all users' privileges. Since we are specifically looking for the current user "hr", we need to filter out using:

`Where-Object { $_.IdentityReferenceName -eq "hr" }`

We're interested in the current user, the vulnerable user, and the privilege assigned. We can filter that out by running:

`Select-Object IdentityReferenceName, ObjectDN, ActiveDirectoryRights`

Now, you can launch the full command:

`Find-InterestingDomainAcl -ResolveGuids | Where-Object { $_.IdentityReferenceName -eq "hr" } | Select-Object IdentityReferenceName, ObjectDN, ActiveDirectoryRights`