email=input("Enter your email address?:").strip()

user_name=email[:email.index("@")]

domain_name=email[email.index("@")+1:]

output="Your Username is '{}' and your domain name is '{}'".format(user_name,domain_name)

print(output)