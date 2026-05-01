
print("Sets:Candidate Skill Matcher")
print("\n")
def skill_analysis(candidates, required):
    
    fully_qualified = sorted(
        name for name, skills in candidates.items()
            if required <= skills
            ) 
    
    best_match = max(sorted(candidates), key=lambda name: len(candidates[name] & required))
    
    unique_skills = {}
    
    for name, skills in candidates.items():
        other_skills = set()
        
        for other_name, other_set in candidates.items():
            if other_name != name:
                other_skills = other_skills|other_set
                
                
        unique = sorted(skills - other_skills)
        
        if unique:
                unique_skills[name] = unique
                    
    return {
        "fully_qualified": fully_qualified,
        "best_match": best_match,
        "unique_skills": unique_skills
    }


candidates = {
    "alice": {"python", "sql", "git", "docker"},
    "bob": {"python", "java", "git"},
    "carol": {"python", "sql", "git", "docker", "kubernetes"},
    "dave": {"java", "c++"},
    "eve": {"python", "sql"},
}

required = {"python", "sql", "git"}

result = skill_analysis(candidates, required)
print(result)


print("\n Recursion Subset Sum")

def subset_sum(nums, target):
    if target == 0:
        return True
    
    if not nums:
        return False
    
    first = nums[0]
    rest = nums[1:]
    
    return subset_sum(rest, target - first) or subset_sum(rest, target)

print(subset_sum([3, 34, 4, 12, 5, 2], 9)) # True (4 + 5 or 3 + 4 + 2)
print(subset_sum([3, 34, 4, 12, 5, 2], 30)) # False
print(subset_sum([1, 2, 3], 0)) # True (empty subset)
print(subset_sum([], 0)) # True
print(subset_sum([], 5)) # False
print(subset_sum([-2, 3, 5], 1)) # True (-2 + 3)
print(subset_sum([1, 2, 3], 7)) # False

