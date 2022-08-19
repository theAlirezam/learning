from bs4 import BeautifulSoup


class CrawlParser:
    def __init__(self):
        self.data = None
        self.soup = None

    def title(self):
        title_tag = self.soup.find('span', attrs={'id': 'titletextonly'})
        if title_tag:
            return title_tag.text

    def price(self):
        price_tag = self.soup.find('span', attrs={'class': 'price'})
        if price_tag:
            return price_tag.text

    def body(self):
        body_tag = self.soup.select_one("#postingbody")
        if body_tag:
            return body_tag.text

    def post_id(self):
        post_id_selector = "p.postinginfo:nth-child(1)"
        post_id_tag = self.soup.select_one(post_id_selector)
        if post_id_tag:
            return post_id_tag.text.replace('post id:', '')

    def created_time(self):
        time_id_selector = ".postinginfos > p:nth-child(2) > time:nth-child(1)"
        time_tag = self.soup.select_one(time_id_selector)
        if time_tag:
            return time_tag.attrs['datetime']

    def images(self):
        images_list = self.soup.find_all('img')
        image_sources = set([img.attrs['src'].replace('50x50c', '600x450') for img in images_list])
        # return [{'url': src} for src in image_sources]
        li = list()
        li.extend(image_sources)
        return li
###################################################
    def set_flag(self, flag=False):               #
        return flag                               #
###################################################
    def parse(self, html_data):
        self.soup = BeautifulSoup(html_data, 'html.parser')
        self.data = dict(
            title=self.title(), price=self.price(), body=None, post_id=self.post_id(), flag=self.set_flag(),
            created_time=self.created_time(), images=self.images()
        )
        return self.data
