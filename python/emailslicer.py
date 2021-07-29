#input user email
email = input("Enter email address: ").strip()

#cut out username i.e. everything that is before the "@" sign
user = email[:email.index("@")]

#get the domain name i.e. everything that is after the "@" sign excluding the "@" sign itself
domain = email[email.index("@")+1:]

#define result and format it
result = "Your username is {} and your domain name is {}".format(user, domain)

#print result
print(result)
