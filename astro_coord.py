import numpy as np 


### converting coordinates 
'''
az - azimuth 
alt - altitude 
ra - right ascension 
ha - hour angle 
dec - declination
phi - equatorial latitude 
LST - local sidereal time 
l - galactic longitude 
b - galactic latitude 
'''


def convert_az_alt_to_ha_dec(az,alt,phi):
    x0 = np.cos(np.radians(alt))*np.cos(np.radians(az))
    x1 = np.cos(np.radians(alt))*np.sin(np.radians(az))
    x2 = np.sin(np.radians(alt))

    R = np.matrix([[-np.sin(np.radians(phi)),0,np.cos(np.radians(phi))],[0,-1,0],[np.cos(np.radians(phi)),0,np.sin(np.radians(phi))]])

    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(np.transpose(R),x)

    ha = float(np.degrees(np.arctan2(xp[1],xp[0]))) + 360
    dec = float(np.degrees(np.arcsin(xp[2]))) 

    return ha, dec

def convert_ha_dec_to_az_alt(ha,dec,phi):
    x0 = np.cos(np.radians(dec))*np.cos(np.radians(ha))
    x1 = np.cos(np.radians(dec))*np.sin(np.radians(ha))
    x2 = np.sin(np.radians(dec))

    R = np.matrix([[-np.sin(np.radians(phi)),0,np.cos(np.radians(phi))],[0,-1,0],[np.cos(np.radians(phi)),0,np.sin(np.radians(phi))]])

    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(R,x)

    az = float(np.degrees(np.arctan2(xp[1],xp[0]))) 
    alt = float(np.degrees(np.arcsin(xp[2]))) 

    return az, alt

def convert_ra_dec_to_ha_dec(ra,dec,LST):
    x0 = np.cos(np.radians(dec))*np.cos(np.radians(ra))
    x1 = np.cos(np.radians(dec))*np.sin(np.radians(ra))
    x2 = np.sin(np.radians(dec))

    R = np.matrix([[np.cos(np.radians(LST)),np.sin(np.radians(LST)),0],[np.sin(np.radians(LST)),-np.cos(np.radians(LST)),0],[0,0,1]])

    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(R,x)

    ha = float(np.degrees(np.arctan2(xp[1],xp[0])))
    dec = float(np.degrees(np.arcsin(xp[2])))
    return ha, dec

def convert_ha_dec_to_ra_dec(ha,dec,LST):
    x0 = np.cos(np.radians(dec))*np.cos(np.radians(ha))
    x1 = np.cos(np.radians(dec))*np.sin(np.radians(ha))
    x2 = np.sin(np.radians(dec))
        
    R = np.matrix([[np.cos(np.radians(LST)),np.sin(np.radians(LST)),0],[np.sin(np.radians(LST)),-np.cos(np.radians(LST)),0],[0,0,1]])

    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(np.transpose(R),x)

    ra = float(np.degrees(np.arctan2(xp[1],xp[0])))
    dec = float(np.degrees(np.arcsin(xp[2])))
    return ra, dec

def convert_ra_dec_to_galactic1950(ra,dec): 
    x0 = np.cos(np.radians(dec))*np.cos(np.radians(ra))
    x1 = np.cos(np.radians(dec))*np.sin(np.radians(ra))
    x2 = np.sin(np.radians(dec))

    R = np.matrix([[-0.066989,-0.872756,-0.483539],[0.492728,-0.450347,0.744585],[-0.867601,-0.188375,0.460200]])

    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(R,x)

    l = float(np.degrees(np.arctan2(xp[1],xp[0]))) + 360
    b = float(np.degrees(np.arcsin(xp[2])))

    return l ,b

def convert_galactic1950_to_ra_dec(l,b): 
    x0 = np.cos(np.radians(b))*np.cos(np.radians(l))
    x1 = np.cos(np.radians(b))*np.sin(np.radians(l))
    x2 = np.sin(np.radians(b))

    R = np.matrix([[-0.066989,-0.872756,-0.483539],[0.492728,-0.450347,0.744585],[-0.867601,-0.188375,0.460200]])

    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(np.transpose(R),x)

    ra =  float(np.degrees(np.arctan2(xp[1],xp[0])))
    dec = float(np.degrees(np.arcsin(xp[2])))

    return ra, dec

def convert_ra_dec_to_galactic2000(ra,dec): 
    x0 = np.cos(np.radians(dec))*np.cos(np.radians(ra))
    x1 = np.cos(np.radians(dec))*np.sin(np.radians(ra))
    x2 = np.sin(np.radians(dec))

    R = np.matrix([[-0.054876,-0.873437,-0.483835],[0.494109,-0.444830,0.746982],[-0.867666,-0.198076,0.455984]])

    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(R,x)

    l = float(np.degrees(np.arctan2(xp[1],xp[0])) ) + 360
    b = float(np.degrees(np.arcsin(xp[2])))

    return l,b

def convert_galactic2000_to_ra_dec(l,b): 
    x0 = np.cos(np.radians(b))*np.cos(np.radians(l))
    x1 = np.cos(np.radians(b))*np.sin(np.radians(l))
    x2 = np.sin(np.radians(b))

    R = np.matrix([[-0.054876,-0.873437,-0.483835],[0.494109,-0.444830,0.746982],[-0.867666,-0.198076,0.455984]])

    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(np.transpose(R),x)

    ra =  float(np.degrees(np.arctan2(xp[1],xp[0])))
    dec = float(np.degrees(np.arcsin(xp[2])))

    return ra, dec


def convert_ra_dec_to_az_alt(ra,dec,LST,phi):
    x0 = np.cos(np.radians(dec))*np.cos(np.radians(ra))
    x1 = np.cos(np.radians(dec))*np.sin(np.radians(ra))
    x2 = np.sin(np.radians(dec))

    R0 = np.matrix([[np.cos(np.radians(LST)),np.sin(np.radians(LST)),0],[np.sin(np.radians(LST)),-np.cos(np.radians(LST)),0],[0,0,1]])
    R1 = np.matrix([[-np.sin(np.radians(phi)),0,np.cos(np.radians(phi))],[0,-1,0],[np.cos(np.radians(phi)),0,np.sin(np.radians(phi))]])



    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(R1,np.dot(R0,x))

    az =  float(np.degrees(np.arctan2(xp[1],xp[0])))
    alt = float(np.degrees(np.arcsin(xp[2])))

    return az, alt


def convert_az_alt_to_ra_dec(az,alt,LST,phi):
    x0 = np.cos(np.radians(alt))*np.cos(np.radians(az))
    x1 = np.cos(np.radians(alt))*np.sin(np.radians(az))
    x2 = np.sin(np.radians(alt))

    R0 = np.matrix([[np.cos(np.radians(LST)),np.sin(np.radians(LST)),0],[np.sin(np.radians(LST)),-np.cos(np.radians(LST)),0],[0,0,1]])
    R1 = np.matrix([[-np.sin(np.radians(phi)),0,np.cos(np.radians(phi))],[0,-1,0],[np.cos(np.radians(phi)),0,np.sin(np.radians(phi))]])



    x = np.matrix([[x0],[x1],[x2]])

    xp = np.dot(np.transpose(R0),np.dot(np.transpose(R1),x))

    ra =  float(np.degrees(np.arctan2(xp[1],xp[0])))
    dec = float(np.degrees(np.arcsin(xp[2])))

    return ra, dec
    







