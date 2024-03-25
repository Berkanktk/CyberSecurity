# Active Directory

Active Directory (AD) is a system mainly used by businesses in Windows environments. It's a centralised authentication system. The Domain Controller (DC) is at the heart of AD and typically manages data storage, authentication, and authorisation within a domain.

You can think of AD as a digital database containing objects like users, groups, and computers, each with specific attributes and permissions. Ideally, it applies the principle of least privilege and uses a hierarchical approach to managing roles and giving authenticated users access to all non-sensitive data throughout the system. For this reason, assigning permissions to users must be approached cautiously, as it can potentially compromise the entire Active Directory. We'll delve into this in the upcoming exploitation section.

> **Use case in short:** Few computers to maintain, changes made on each. But in larger companies, this process is automated.

# Active Directory Components
The core of any Windows Domain is the Active Directory Domain Service (AD DS). This service acts as a catalogue that holds the information of all of the "objects" that exist on your network. Amongst the many objects supported by AD, we have users, groups, machines, printers, shares and many others. Let's look at some of them:
1. **Users**: These are the people who use the network. They can log in to the network and access resources.
2. **Groups**: These are collections of users. They are used to simplify the management of permissions and access to resources.
3. **Computers**: These are the machines that are part of the network. They can be desktops, laptops, servers, etc.
4. **Organizational Units (OUs)**: These are containers that hold objects. They are used to organize objects in a logical way.
5. **Domains**: These are logical groupings of objects. They are used to manage the objects in a more efficient way.
6. **Domain Controllers**: These are the servers that run the AD DS service. They are responsible for authenticating users and managing the objects in the domain.
7. **Sites**: These are physical groupings of objects. They are used to manage the objects in a more efficient way.
8. **Trusts**: These are relationships between domains. They are used to allow users in one domain to access resources in another domain.
9. **Schema**: This is the definition of all the objects that can exist in the AD DS. It is used to define the structure of the AD DS.
10. **Forest**: This is a collection of domains. It is used to manage the objects in a more efficient way.
11. **Group Policy Objects (GPOs)**: These are collections of settings that can be applied to objects. They are used to manage the objects in a more efficient way.
12. **Replication**: This is the process of copying objects between domain controllers. It is used to ensure that all domain controllers have the same information.
13. **Global Catalog**: This is a special domain controller that holds a copy of all the objects in the forest. It is used to speed up searches for objects.
14. **Lightweight Directory Access Protocol (LDAP)**: This is the protocol used to access the AD DS. It is used to manage the objects in a more efficient way.
15. **Kerberos**: This is the authentication protocol used by AD DS. It is used to authenticate users and manage the objects in the domain.

## Security Groups vs OUs

You are probably wondering why we have both groups and OUs. While both are used to classify users and computers, their purposes are entirely different:

- **OUs** are handy for **applying policies** to users and computers, which include specific configurations that pertain to sets of users depending on their particular role in the enterprise. Remember, a user can only be a member of a single OU at a time, as it wouldn't make sense to try to apply two different sets of policies to a single user.
- **Security Groups**, on the other hand, are used to **grant permissions over resources**. For example, you will use groups if you want to allow some users to access a shared folder or network printer. A user can be a part of many groups, which is needed to grant access to multiple resources.

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