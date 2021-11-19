from pyshorteners import Shortener


def short(link):
    results = {}
    
    # Chilp.it shorten
    try:
        s = Shortener()
        url = s.chilpit.short(link)
        results["chilp.it"] = url
    except Exception as error:
        pass
    
    # Click.ru shorten
    try:
        s = Shortener()
        url = s.clckru.short(link)
        results["click.ru"] = url
    except:
        pass
    
    # Da.gd shorten
    try:
        s = Shortener()
        url = s.dagd.short(link)
        results["da.gd"] = url
    except:
        pass
    
    # Git.io shorten
    if "github.com" in link or "github.io" in link:
        try:
            s = Shortener()
            url = s.gitio.short(link)
            results["git.io"] = url
        except:
            pass
    
    # Is.gd shorten
    try:
        s = Shortener()
        url = s.isgd.short(link)
        results["is.gd"] = url
    except:
        pass
    
    # osdb.link shorten
    try:
        s = Shortener()
        url = s.osdb.short(link)
        results["osdb.link"] = url
    except:
        pass
    
    # Qps.ru shorten
    try:
        s = Shortener()
        url = s.qpsru.short(link)
        results["qps.ru"] = url
    except:
        pass
    
    # 0x0.st shorten
    try:
        s = Shortener(domain='https://0x0.st')
        url = s.nullpointer.short(link)
        results["0x0.st"] = url
    except:
        pass
    
    # ttm.sh shorten
    try:
        s = Shortener(domain='https://ttm.sh')
        url = s.nullpointer.short(link)
        results["ttm.sh"] = url
    except:
        pass
    
    return results
