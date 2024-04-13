import csv

book_titles = []
authors = []
types = []
image_links = []
descriptions = []
prices = []
stars = []
reviews_1 = []
reviews_2 = []
sellers = []
stocks = []
books_info = []
books = []

with open('Book_Data_2.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract data from each row and create a dictionary for the book
        book_info = {
            'Book Title': row['Book Title'],
            'Author': row['Author'],
            'Type': row['Type'],
            'Image Link': row['Image Link'],
            'Description': row['Description'],
            'Price': row['Price'],
            'Stars': row['Stars'],
            'Review1': row['Review1'],
            'Review2': row['Review2'],
            'Seller 1': row['Seller 1'],
            'Seller 2': row['Seller 2'],
            'Seller 3': row['Seller 3'],
            'Stock': row['Stock'],
            'College 1':row['College 1'],
            'College 2': row['College 2'],
            'College 3': row['College 3']
        }
        # Append the book information dictionary to the list
        books_info.append(book_info)
        books.append(book_info)
