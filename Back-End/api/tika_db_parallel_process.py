from tika import parser
from mysql import connector
from multiprocessing import Pool


def tika_parser(file_path):
    # Extract text from document
    content = parser.from_file(file_path)
    if 'content' in content:
        text = content['content']
        print(text)
    else:
        return
    # Convert to string
    text = str(text)
    # Ensure text is utf-8 formatted
    safe_text = text.encode('utf-8', errors='ignore')
    # # Escape any \ issues
    print("safe text :",safe_text)
    safe_text = str(safe_text).replace('\"',"\'")
    # .replace("\\\", "\\\")
    # .replace('"', "\"")
    # Connect and send to database (in multiprocessing must re-connect each time)
    print('Start processing..')
    print("...............................")
    print(safe_text)

    update_query = f'UPDATE api_fileupload SET content_pdf = "{safe_text}" WHERE id =1;'
    connection = connector.connect(database='melondataDB', user='melon', password='Melon123!')
    cursor = connection.cursor()
    cursor.execute(update_query)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    # Retrieve file paths from database
    query = 'SELECT pdf_doc_path from api_fileupload;'
    cnx = connector.connect(database='melondataDB', user='melon', password='Melon123!')
    cur = cnx.cursor()
    cur.execute(query)
    paths = cur.fetchall()
    cur.close()
    cnx.close()

    pool = Pool()
    pool.map(tika_parser, paths)