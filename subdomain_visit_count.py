"""
https://leetcode.com/problems/subdomain-visit-count/
A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", 
at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a 
domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), 
followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, 
(in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" 
will also be visited. So they will all be visited 9001 times.

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. 
For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
"""
from collections import defaultdict
def subdomainVisits(cpdomains):
    domainCount = defaultdict(int) #initiates entries with 0

    #for each cpdomains
    for cpd in cpdomains:
        numVisit = int(cpd.split(' ')[0]) #visit count for this cpdomain address 
        domainAddresses = cpd.split(' ')[1].split('.') #domain address ex: ["google", "mail", "com"] for google.mail.com
        
        for i in range(len(domainAddresses)):
            d = '.'.join(domainAddresses[i:]) #joins addresses back together ex: "google.mail.com"
            domainCount[d] += numVisit #adds number of visits to this address
    
    result = []
    #turn domainCount dictionary into an array string 
    for subDomain, visitCount in domainCount.items():
        result.append(' '.join([str(visitCount), subDomain]))
    return result

input_1 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(input_1))

input_2 = ["9001 discuss.leetcode.com"]
print(subdomainVisits(input_2))
