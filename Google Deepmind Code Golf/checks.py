
import json
import copy
with open('task008.json','r') as f:
    data=json.load(f)

# Function to check each set
def check_set(dataset):
    for idx,entry in enumerate(dataset):
        inp=copy.deepcopy(entry['input'])  # deep copy so original is not modified
        out=entry['output']
        result=p(inp)
        if result!=out:
            print(f"Entry {idx}: FAIL")
            print("Result:")
            for r in result:
                print(r)
            print("Expected:")
            for r in out:
                print(r)
        #else:
        #    print(f"Entry {idx}: FAIL")
        #    print("Result:")
        #    for r in result:
        #        print(r)
        #    print("Expected:")
        #    for r in out:
        #        print(r)

# Run checks
for key in ['train','test','arc-gen']:
    print(f"\nChecking {key} set:")
    check_set(data[key])