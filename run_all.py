import subprocess

scripts = [
    "H&M CordSets.py", "H&M LongSleeveDresses.py", "H&M Maxi Dresses.py","H&M Midi Dresses.py","H&M Medium Dresses.py","H&M Shirt Dresses.py","H&M Small.py",
    "H&M WomensTops&tshirts.py"
]

for script in scripts:
    subprocess.Popen(["python", script])
