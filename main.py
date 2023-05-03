from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

#--------------------beautiful soup Stuff--------------

response = requests.get("https://www.marykay.com/en-us/products/new-products")
mary_kay_web = response.text

soup = BeautifulSoup(mary_kay_web, "html.parser")


# -------------------HOW MANY PRODUCTS---------------------------

nr_of_products = soup.find(class_="total-products")
nr_of_products = int(nr_of_products.text[0:3])

# -------------------ALL PRODUCT IMAGES IN A LIST------------------------------

all_imgs = []
new_all_products = soup.findAll('img')

for image in new_all_products:
    all_imgs.append(image['src'])

new_pr_imgs_t1 = all_imgs[6:]
new_pr_imgs = new_pr_imgs_t1[:nr_of_products]

# ----------------PRODUCTS NAME--------------------------
products_names = []

products_name_list = soup.findAll(class_='product-name')
for product_name in products_name_list:
    product_names = product_name.text
    products_names.append(product_names)
    products_names = list(map(lambda x: x.replace('®', ''), products_names))
    products_names = list(map(lambda x: x.replace('†', ''), products_names))
    products_names = list(map(lambda x: x.replace('™', ''), products_names))
# ----------------PRODUCTS PRICE----------------------
products_prices = []
rounded_products_prices = []

products_prices_list = soup.findAll(class_='price')
for product_price in products_prices_list:
    product_prices = product_price.text
    products_prices.append(product_prices)

products_prices = list(map(lambda x: x.replace('\n', ''), products_prices))
products_prices = list(map(lambda x: x.replace('$', ''), products_prices))


for number in products_prices:
    float_number = float(number)
    round_number = round(float_number)
    str_rounded_number = str(round_number)
    str_rounded_number_wd = ("$"+str_rounded_number)
    rounded_products_prices.append(str_rounded_number_wd)


# -----------------INFO FOR MORE ABOUT PRODUCT--------

all_the_new_products_links = []

all_about_new_prcd = soup.find_all('a', {'class': 'product-name'})
all_the_new_product_link = [a['href'] for a in all_about_new_prcd]

for prdct_link in all_the_new_product_link:
    full_prdct_link = "https://www.marykay.com" + prdct_link
    all_the_new_products_links.append(full_prdct_link)

# ----------------WORK TIME BABY----------------------

with open("card_blueprint", 'r') as card_txt:
    card_html = card_txt.read()
    lonfoto = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
                '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53',
                '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
                '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87',
                '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
    a = 0
    trc = []
    for i in range(nr_of_products):
        new_card_html_id = card_html.replace("[id_nr]", lonfoto[a])
        new_card_html_id_img = new_card_html_id.replace("[img_url]", new_pr_imgs[a])
        new_card_html_id_img_name = new_card_html_id_img.replace("[Card_title]", products_names[a])
        new_card_html_id_img_name_price = new_card_html_id_img_name.replace("[price]", rounded_products_prices[a])
        new_card_html_id_img_name_price_prdctlink = new_card_html_id_img_name_price.replace("[product_link]", all_the_new_products_links[a])
        a = a + 1
        trc.append(new_card_html_id_img_name_price_prdctlink)




def listToString(s):
    str1 = ""
    for ele in s:
         str1 += ele
    return str1


with open("templates/fresh_products.html", "w") as file:
    file.write(listToString(trc))


# -----------------------------------------------------

# --------------------------------------------------

# -----------------BEEEST sellers code--------------------------

# --------------------beautiful soup Stuff--------------

response_bs = requests.get("https://www.marykay.com/en-us/products/best-sellers?iad=hp_std_product_color_bestsellersfanorama_223")
mary_kay_web_bs = response_bs.text

soup_bs = BeautifulSoup(mary_kay_web_bs, "html.parser")


# -------------------HOW MANY PRODUCTS---------------------------

nr_of_products = soup_bs.find(class_="total-products")
nr_of_products = int(nr_of_products.text[0:3])

# -------------------ALL PRODUCT IMAGES IN A LIST------------------------------

all_imgs = []
new_all_products = soup_bs.findAll('img')

for image in new_all_products:
    all_imgs.append(image['src'])

new_pr_imgs_t1 = all_imgs[6:]
new_pr_imgs = new_pr_imgs_t1[:nr_of_products]

# ----------------PRODUCTS NAME--------------------------
products_names = []

products_name_list = soup.findAll(class_='product-name')
for product_name in products_name_list:
    product_names = product_name.text
    products_names.append(product_names)
    products_names = list(map(lambda x: x.replace('®', ''), products_names))
    products_names = list(map(lambda x: x.replace('†', ''), products_names))
    products_names = list(map(lambda x: x.replace('™', ''), products_names))
# ----------------PRODUCTS PRICE----------------------
products_prices = []
rounded_products_prices = []

products_prices_list = soup_bs.findAll(class_='price')
for product_price in products_prices_list:
    product_prices = product_price.text
    products_prices.append(product_prices)

products_prices = list(map(lambda x: x.replace('\n', ''), products_prices))
products_prices = list(map(lambda x: x.replace('$', ''), products_prices))



for number in products_prices:
    float_number = float(number)
    round_number = round(float_number)
    str_rounded_number = str(round_number)
    str_rounded_number_wd = ("$"+str_rounded_number)
    rounded_products_prices.append(str_rounded_number_wd)


# -----------------INFO FOR MORE ABOUT PRODUCT--------
all_the_new_products_links = []

all_about_new_prcd = soup_bs.find_all('a', {'class': 'product-name'})
all_the_new_product_link = [a['href'] for a in all_about_new_prcd]

for prdct_link in all_the_new_product_link:
    full_prdct_link = "https://www.marykay.com" + prdct_link
    all_the_new_products_links.append(full_prdct_link)
# ----------------WORK TIME BABY----------------------
with open("card_blueprint", 'r') as card_txt:
    card_html = card_txt.read()
    lonfoto = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
                '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53',
                '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
                '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87',
                '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
    a = 0
    trc = []
    for i in range(nr_of_products):
        new_card_html_id = card_html.replace("[id_nr]", lonfoto[a])
        new_card_html_id_img = new_card_html_id.replace("[img_url]", new_pr_imgs[a])
        new_card_html_id_img_name = new_card_html_id_img.replace("[Card_title]", products_names[a])
        new_card_html_id_img_name_price = new_card_html_id_img_name.replace("[price]", rounded_products_prices[a])
        new_card_html_id_img_name_price_prdctlink = new_card_html_id_img_name_price.replace("[product_link]", all_the_new_products_links[a])
        a = a + 1
        trc.append(new_card_html_id_img_name_price_prdctlink)


def listToString(s):
    str1 = ""
    for ele in s:
         str1 += ele
    return str1


with open("templates/best_sellers.html", "w") as file:
    file.write(listToString(trc))

# -----------------THE ROUTES-------------------------

@app.route("/")
def hero():
    return render_template("hero.html")


if __name__ == '__main__':
    app.run()