# -*- coding: utf-8 -*-
{
    'name': "Band Manager",
    'summary': """This module allows to manage music bands""",
    'description': """
    
Band Manager is a solution for the music bands management for producers or band members.
With this module you can:

1. Manage several (many) music bands: enter members, songs, setlists, rehearsals and shows.
2. Enter a song with duration, version, lyrics and other information.
3. Enter a setlist of a selected songs.
4. Enter a rehearsals and shows with dates, locations, members, equipment, setlists ant other information.
5. Enter the band members with abilities, status and instruments.
6. Print lyrics of the selected song.
7. Print selected setlist of songs.
 
Icons made by Freepik (http://www.freepik.com) from www.flaticon.com (https://www.flaticon.com/) is licensed by "Creative Commons BY 3.0" (http://creativecommons.org/licenses/by/3.0/).
                
    """,

    'author': "Donatas Noreika",
    'support': 'programosjusuverslui@gmail.com',
    'website': "http://programosverslui.wordpress.com",
    'license': 'AGPL-3',
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '1.2.1',
    'images': ['static/images/main_screenshot.png', 'static/images/main_1.png', 'static/images/main_2.png', 'static/images/main_3.png', 'static/images/main_4.png', 'static/images/main_5.png', 'static/images/main_6.png', 'static/images/main_7.png'],

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/bands_view.xml',
        'views/songs_view.xml',
        'views/rehearsals_view.xml',
        'views/shows_view.xml',
        'views/setlists_view.xml',
        'views/members_view.xml',
        'views/members_lists_view.xml',
        'views/equipment_lists_view.xml',
        'views/instruments_view.xml',
        'report/lyrics_export.xml',
        'report/setlist_export.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
