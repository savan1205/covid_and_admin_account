from odoo import fields, http, SUPERUSER_ID, _
from odoo.http import request

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class UserProducts(http.Controller):
    @http.route('/my/products', type='http', auth="public", website=True)
    def get_user_products(self, page=1, date_begin=None, date_end=None, sortby=None, **kwargs):
        partner = request.env.user.partner_id
        user_productss = partner.user_id

        values = {
            'user': user_productss,
            'page_name': 'products',
        }
        Product = request.env['user.products']

        # domain = self._prepare_quotations_domain(partner)

        # searchbar_sortings = self._get_sale_searchbar_sortings()

        # default sortby order
        # if not sortby:
        #     sortby = 'date'
        # sort_order = searchbar_sortings[sortby]['order']

        # if date_begin and date_end:
        #     domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]
        #
        # # count for pager
        # quotation_count = SaleOrder.search_count(domain)
        # make pager
        product_count = request.env['user.products'].search_count([])
        print("=======", product_count)
        pager = portal_pager(
            url="/my/products",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=product_count,
            page=page,
            # step=self._items_per_page
        )
        # search the count to display, according to the pager data
        products = Product.search([])
        print("++++++++++++++++252525252", products)
        # request.session['my_quotations_history'] = quotations.ids[:100]
        values.update({
            'date': date_begin,
            'products': products.sudo(),
            # 'products': products,
            'pager': pager,
            'default_url': '/my/products',
            # 'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render('covid.portal_my_products', values)

    @http.route('/my/products/<model("user.products"):product>', type='http', auth="public", website=True)
    def product_details(self, product, **kw):
        return request.render('covid.product_details', {'product': product})

