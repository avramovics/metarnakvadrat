
# Between 2*30 = 60 and 60 + 30 = 90

# if i > a and < b then get "Ruler" 

# Find the rooler of 1 and 7 house 
#if in Conjunction  with 1 and 7th house or partners roolers 
#this is an indicator of marriage in synastry.



#these houses represent analogue house
analog_houses = [
    {"House": 1, "Sign": "Aries", "Ruler": ["Mars"]},
    {"House": 2, "Sign": "Taurus", "Ruler": ["Venus"]},
    {"House": 3, "Sign": "Gemini", "Ruler": ["Mercury"]},
    {"House": 4, "Sign": "Cancer", "Ruler": ["Moon"]},
    {"House": 5, "Sign": "Leo", "Ruler": ["Sun"]},
    {"House": 6, "Sign": "Virgo", "Ruler": ["Mercury"]},
    {"House": 7, "Sign": "Libra", "Ruler": ["Venus"]},
    {"House": 8, "Sign": "Scorpio", "Ruler": ["Pluto", "Mars"]},
    {"House": 9, "Sign": "Sagittarius", "Ruler": ["Jupiter"]},
    {"House": 10, "Sign": "Capricorn", "Ruler": ["Saturn"]},
    {"House": 11, "Sign": "Aquarius", "Ruler": ["Uranus", "Saturn"]},
    {"House": 12, "Sign": "Pisces", "Ruler": ["Neptune", "Jupiter"]}
]


sexuality = [
  {
    "algo" : "aspect",
    "exact_time":False,  
    "Planets/cusps": ["Mars", "Mars"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Harmonious and passionate connection, promoting strong sexual compatibility."
  },
  {
    "algo" : "aspect",
    "exact_time":False,
    "Planets/cusps": ["Venus", "Mars"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Balanced blend of desire and affection, contributing to a fulfilling sexual relationship."
  },
  {
    "algo" : "aspect", 
    "exact_time":False,   
    "Planets/cusps": ["Venus", "Venus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Harmonious and affectionate connection, fostering a pleasurable sexual bond."
  },
  {
    "algo" : "aspect", 
    "exact_time":False,   
    "Planets/cusps": ["Pluto", "Mars"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Intense and transformative sexual connection, deepening the bond between partners."
  },
  {
    "algo" : "aspect",
    "exact_time":False,  
    "Planets/cusps": ["Pluto", "Venus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Passionate and transformative sexual relationship, fostering emotional and physical intimacy."
  },
  {
    "algo" : "aspect",  
    "exact_time":False,  
    "Planets/cusps": ["Sun", "Mars"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Energetic and assertive connection, contributing to a dynamic and passionate sexual life."
  },
  {
    "algo" : "aspect",  
    "exact_time":True,  
    "Planets/cusps": ["Moon", "Mars"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Emotionally fulfilling and stimulating sexual connection, promoting a deep bond."
  },
  {
    "algo" : "aspect", 
     "exact_time":True,   
    "Planets/cusps": ["Mars", "Ascendant"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Dynamic and arousing connection, leading to a vibrant and fulfilling sexual relationship."
  },
  {
    "algo" : "aspect",
     "exact_time":True,    
    "Planets/cusps": ["Venus", "Ascendant"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Harmonious and sensual connection, fostering a pleasurable and enjoyable sexual bond."
  },
  {
    "algo" : "position",  
     "exact_time":True,  
    "Planets/cusps": ["Sun", 8],
    "Aspects": ["Conjunction "],
    "Description": "Deep and transformative sexual connection, leading to profound intimacy and bonding."
  },
  {
    "algo" : "position",
     "exact_time":True,  
    "Planets/cusps": ["Moon", 8],
    "Aspects": ["Conjunction "],
    "Description": "Emotionally intense and transformative sexual bond, deepening the connection between partners."
  },
  {
    "algo" : "position",
     "exact_time":True,  
    "Planets/cusps": ["Pluto", 8],
    "Aspects": ["Conjunction "],
    "Description": "Powerful and transformative sexual relationship, leading to deep emotional and physical connection."
  },
    {
    "algo" : "position",
     "exact_time":True,  
    "Planets/cusps": ["Venus", 8],
    "Aspects": ["Conjunction "],
    "Description": "Powerful and transformative sexual relationship, leading to deep emotional and physical connection."
  },
    {
    "algo" : "position",
     "exact_time":True,  
    "Planets/cusps": ["Mars", 8],
    "Aspects": ["Conjunction "],
    "Description": "Powerful and transformative sexual relationship, leading to deep emotional and physical connection."
  }

]




marriage = [
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Juno", "Juno"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Harmonious and fated connection, indicating a strong potential for a meaningful and lasting marriage."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Venus", "Venus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Affectionate and loving connection, fostering a deep bond and compatibility in marriage."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Sun", "Venus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Harmonious and supportive connection, contributing to a loving and fulfilling marriage."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Moon", "Moon"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Emotionally supportive and nurturing connection, indicating a strong bond in marriage."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Saturn", "Saturn"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Stable and committed connection, suggesting a long-lasting and enduring marriage."
  },
  
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Sun", "Descendant"],
    "Aspects": ["Conjunction"],
    "Description": "Harmonious and supportive connection, indicating a positive influence on marriage and partnerships."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Moon", "Descendant"],
    "Aspects": ["Conjunction"],
    "Description": "Emotionally supportive and nurturing connection, suggesting a strong bond in marriage and partnerships."
  },
 
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Venus", "Descendant"],
    "Aspects": ["Conjunction"],
    "Description": "Affectionate and loving connection, fostering a deep bond and compatibility in marriage and partnerships."
  }
  
  ,{
    "algo" : "position",
    "exact_time":False, 
    "Planets/cusps": ["Sun", 7],
    "Aspects": [],
    "Description": "Harmonious and supportive connection, indicating a positive influence on marriage and partnerships."
  },
  {
    "algo" : "position",
    "exact_time":False, 
    "Planets/cusps": ["Venus", 7],
    "Aspects": [],
    "Description": "Affectionate and loving connection, fostering a deep bond and compatibility in marriage and partnerships."
  },
  {
    "algo" : "position",
    "exact_time":False, 
    "Planets/cusps": ["Mars", 7],
    "Aspects": [],
    "Description": "Dynamic and energetic connection, contributing to a vibrant and fulfilling marriage and partnerships."
  },
  {
    "algo" : "position",
    "exact_time":False, 
    "Planets/cusps": ["Jupiter", 7],
    "Aspects": [],
    "Description": "Expansive and positive connection, indicating growth and fulfillment in marriage and partnerships."
  }
]


friendship = [
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Sun", "Mercury"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Harmonious communication and understanding, supporting a strong friendship."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mercury", "Mercury"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Mutual intellectual connection, fostering a close and communicative friendship."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Venus", "Mars"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Balanced blend of passion and affection, contributing to a friendly and lively connection."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Sun", "Uranus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Innovative and unique friendship, characterized by shared interests and open-mindedness."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Moon", "Uranus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Emotionally stimulating friendship with a sense of spontaneity and excitement."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mercury", "Uranus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Intellectually stimulating and unconventional friendship, fostering mutual understanding."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Venus", "Uranus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Unconventional and exciting friendship, characterized by shared values and interests."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mars", "Uranus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Dynamic and energetic friendship with shared goals and a sense of adventure."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Jupiter", "Uranus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Expansive and adventurous friendship, marked by shared ideals and a positive outlook."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Saturn", "Uranus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Balanced and stable friendship with a blend of tradition and innovation."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Uranus", "Uranus"],
    "Aspects": ["Conjunction ", "Trine", "Sextile"],
    "Description": "Mutually stimulating and unique friendship, characterized by shared interests and a sense of individuality."
  }
]


# Red Flags and When to Run
toxic = [
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Venus", "Saturn"],
    "Aspects": ["Square", "Opposition"],
    "Description": "This aspect can bring up challenges related to control, authority, and frustration in the realm of values and relationships. It may manifest as power struggles or conflicts in how values and relationships are managed."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Moon", "Saturn"],
    "Aspects": ["Square", "Opposition"],
    "Description": "In synastry, this aspect can bring up issues related to emotional expression, nurturing, and responsibilities. It may manifest as conflicts in how emotions and responsibilities are balanced between partners."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mercury", "Mars"],
    "Aspects": ["Square", "Opposition"],
    "Description": "In the realm of communication and intellectual pursuits, this aspect can bring up challenges. It may manifest as conflicts in how thoughts and actions are expressed, potentially leading to misunderstandings."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mars", "Pluto"],
    "Aspects": ["Square", "Opposition"],
    "Description": "This synastry aspect can bring up intense power struggles and conflicts between partners. It may manifest as challenges in asserting oneself and dealing with transformative experiences in the relationship."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mercury", "Mercury"],
    "Aspects": ["Square", "Opposition"],
    "Description": "Hard Mercury-Mercury aspects in synastry can bring challenges in communication and understanding between partners. It may manifest as conflicts in exchanging ideas and opinions."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mars", "Saturn"],
    "Aspects": ["Square", "Opposition"],
    "Description": "In synastry, conflict between Mars and Saturn can lead to issues related to control, authority, and frustration. It may manifest as power struggles or conflicts in how actions and responsibilities are carried out."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mars", "Mars"],
    "Aspects": ["Square", "Opposition"],
    "Description": "Mars Square Mars in synastry can bring challenges in asserting oneself and dealing with conflicts between partners. It may manifest as intense competition and clashes in desires and actions."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Sun", "Sun"],
    "Aspects": ["Square", "Opposition"],
    "Description": "In synastry, Sun Square Sun and Sun Opposition Sun can bring plenty of challenges. It may manifest as conflicts in identity, self-expression, and clashes in personal goals and ambitions between partners."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mars", "Saturn"],
    "Aspects": ["Square", "Opposition"],
    "Description": "In synastry, there might be tensions between the desire for bold, assertive moves (Mars) and the need for structure, control, or a more cautious approach (Saturn). This can lead to power struggles or conflicts in reconciling these contrasting energies."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mars", "Uranus"],
    "Aspects": ["Square", "Opposition"],
    "Description": "This synastry aspect can bring up issues related to impulsiveness, rebellion, and assertiveness. It may manifest as conflicts in how actions and individuality are expressed between partners."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps": ["Mars", "Neptune"],
    "Aspects": ["Square", "Opposition"],
    "Description": "In synastry, this aspect can bring challenges in assertiveness and dealing with illusions. It may manifest as conflicts in actions and desires, influenced by idealistic or deceptive tendencies."
  },
  {
    "algo" : "aspect",
    "exact_time":False, 
    "Planets/cusps" : ["Mars", "Pluto"],
    "Aspects" : ["Square", "Opposition"],
    "Description" : "This synastry aspect can bring up intense power struggles and conflicts. It may manifest as challenges in asserting oneself and dealing with transformative experiences between partners."
  }
]

kids=[]

