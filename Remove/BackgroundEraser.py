from rembg import remove

input_path = "nama.jpg"

output_path = "output1.png"

with open(input_path, "rb") as i:
    with open(output_path, "wb") as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)