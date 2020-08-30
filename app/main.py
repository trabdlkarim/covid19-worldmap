#!/usr/bin/env python
#-*- coding: utf-8 -*-



from app import create_app


def run():
    webapp = create_app()
    webapp.run(debug=True)



if __name__=="__main__":
    run()
