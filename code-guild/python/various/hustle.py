"""
Python module that provides a high level API for checking
if Grant Douglas Holly was infact "hustlin"
"""
import webbrowser

def check_hustle(day):
    """
    @day -> any point in time in which hustle status is to be checked
    return -> hustle status
    """
    
    if day:
	return webbrowser.open("https://www.youtube.com/watch?v=5betFZRICVg")

