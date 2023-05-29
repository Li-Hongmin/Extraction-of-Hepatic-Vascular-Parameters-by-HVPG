#%%
import os
import vmtk
# Set the path to the vmtkcenterlines.py file
# find vmtkcenterlines.py in vmtk package

vmtkcenterlines_path = os.path.join(os.path.dirname(vmtk.__file__), "vmtkcenterlines.py")
print(vmtkcenterlines_path)
#%%

# Read the contents of the vmtkcenterlines.py file
with open(vmtkcenterlines_path, 'r') as f:
    contents = f.read()

# Replace len(self.SourcePoints)/3 with int(len(self.SourcePoints)/3)
new_contents = contents.replace("len(self.TargetPoints)/3", "int(len(self.TargetPoints)/3)")
new_contents = contents.replace("len(self.SourcePoints)/3", "int(len(self.SourcePoints)/3)")

# Write the modified contents back to the vmtkcenterlines.py file
with open(vmtkcenterlines_path, 'w') as f:
    f.write(new_contents)
# %%
