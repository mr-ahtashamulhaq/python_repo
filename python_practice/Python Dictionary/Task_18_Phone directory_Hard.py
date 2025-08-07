"""Given a list of contacts contact[] of length n where each contact is a string which exist in a phone directory and a query string s.

 The task is to implement a search query for the phone directory. Run a search query for each prefix p of the query string s (i.e. from  index 1 to |s|) that prints all the distinct contacts which have the same prefix as p in lexicographical increasing order.

Note: If there is no match between query and contacts, print "0"."""

class PhoneDirectory:
    def displayContacts(self, contacts, query):
        result = []
        contacts = sorted(set(contacts))

        for i in range(1, len(query) + 1):
            prefix = query[:i]
            matches = []

            for contact in contacts:
                if contact.startswith(prefix):
                    matches.append(contact)

            if matches:
                result.append(matches)
            else:
                result.append(["0"])
        
        return result


contacts = ["geeikistest", "geeksforgeeks", "geeks", "geek", "geezer"]
query = "geeips"

pd = PhoneDirectory()
res = pd.displayContacts(contacts, query)

for level in res:
    print(' '.join(level))