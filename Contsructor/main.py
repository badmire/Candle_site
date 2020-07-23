"""

"""

import csv
from yattag import Doc

# Global Variables
pages = dict()
categories = dict()
csvfile = "sample_data.csv"

with open(csvfile) as target:
    reader = csv.DictReader(target, delimiter=',', quotechar='"')
    for row in reader:
        pages[row["Title"]] = row


for page in pages.values():
    print()
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head', lang='en'):
            doc.stag('link', rel='stylesheet', href='../../css/general.css')
            doc.stag('link', rel='stylesheet', href='../../css/item_template.css')
        with tag('body'):
            # Create top nav bar
            with tag('a'):
                doc.stag('img', id='banner', src='../../banner_v1-01.jpg')
            with tag('div', id='nav_bar'):
                with tag('ul', klass='topnav'):
                    with tag('li'):
                        with tag('a', href='./home.htm'):
                            text('Home')
                    with tag('li'):
                        with tag('a', href='./shop.htm', id='active'):
                            text('Shop by Category')
                    with tag('li'):
                        with tag('a', href='./by_mail.htm'):
                            text('Order by Mail')
                    with tag('li'):
                        with tag('a', href='./about.htm'):
                            text('About')
            
            # Create Main Content space
            with tag('div', id='main_content'):
                # Create store nav
                pass

                # Create visual section
                with tag('div', id='visual'):
                    with tag('div', id='name'):
                        with tag('a'):
                            text(page["Title"])
                    with tag('div', id='pic_container'):
                        doc.stag('img', id='pic', src=f'../../images/{page["Picture"]}.jpg')
                
                # Create order section
                with tag('div', id='order'):
                    with tag('h1'):
                        text(f'${page["Price"]}')
                    with tag('div', id='dropdown'):
                        with tag('select'):
                            for i in range(1,10):
                                with tag('option'):
                                    text(i)
                    doc.stag('br')

                    #TO DO: ADD BUTTON FUNCTIONALITY
                    with tag('div', klass='button'):
                        with tag('button'):
                            text('Add to cart')



                # Create description section
                with tag('div', id='description'):
                    with tag('p'):
                        text(page["Description"])

    with open(f'./output/{page["Title"]}.htm', 'w') as final:
        final.write(doc.getvalue())