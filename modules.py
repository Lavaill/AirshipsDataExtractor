cannon = """[
	{
		"name": "FLIPPED_CANNON",
		"flippedFrom": "CANNON"
	},
	{
		"name": "CANNON",
		"variants": ["CANNON_WDECK"],
		"categories": ["BASIC", "WEAPONS"], "sort": 10,
		"required": "CANNONS",
		"isWeapon": true, "isGun": true, "isCannon": true,
		"w": 2, "h": 1,
		"appearance": {
			"base": { "src": "modules", "x": 40, "y": 3, "w": 2 },
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": { "src": "modules", "x": 40, "y": 7, "w": 2 } },
				{ "bonuses": [ "DECK_GUNS" ], "value": { "src": "modules", "x": 40, "y": 5, "w": 2 } },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": { "src": "modules", "x": 40, "y": 4, "w": 2 } }
			]
		},
		"frontOnly": true,
		"moveDelay": 800,
		"hp": 100,
		"fireHP": 60,
		"explodeHP": { "base": 30, "SAFER_CANNONS": 0 },
		"explodeDmg": { "base": 35, "SAFER_CANNONS": 0 },
		"weight": 70,
		"cost": 75,
		"crew": 1,
		"recommendedCrew": 2, "recommendedGuards": 1,
		"penDmg": { "base": 40, "multipliers": { "INCREASED_CANNON_DAMAGE": 1.2, "MASTER_METALLURGIST": 1.2, "HEAVY_GUNNERY": 1.5 } },
		"reload": { "base": 3500, "multipliers": { "FASTER_CANNON_RELOAD": 0.8, "HEAVY_GUNNERY": 1.3 } },
		"clip": 1,
		"recoilForce": 1.2,
		"inaccuracy": { "base": 0.0014, "PRECISE_GUNNERY": 0.0007 },
		"optimumRange": 400,
		"fireArc": { "direction": "forwards", "degrees": 70 },
		"muzzleCenterX": {
			"base": 1.594,
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": 1.437 },
				{ "bonuses": [ "DECK_GUNS" ], "value": 1.437 },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": 1.562 }
			]
		},
		"muzzleCenterY": {
			"base": 0.531,
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": 0.562 },
				{ "bonuses": [ "DECK_GUNS" ], "value": 0.562 },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": 0.562 }
			]
		},
		"muzzleLength": {
			"base": 0.969,
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": 1.594 },
				{ "bonuses": [ "DECK_GUNS" ], "value": 1.625 },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": 1.5 }
			]
		},
		"hitParticle": "damaged_spark",
		"weaponAppearance": {
			"base": {
				"back": { "src": "modules", "x": 52, "y": 10 },
				"shot": { "src": "modules", "x": 149, "y": 482, "w": 3, "h": 3 },
				"barrel": { "src": "modules", "x": 330, "y": 791, "w": 29, "h": 13 },
				"barrelX": 11, "barrelY": 2,
				"recoil": 6
			},
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": {
					"back": { "src": "modules", "x": 48, "y": 14 },
					"shot": { "src": "modules", "x": 155, "y": 488, "w": 4, "h": 2 },
					"barrel": { "src": "modules", "x": 551, "y": 824, "w": 49, "h": 9 },
					"barrelX": -1.5, "barrelY": 4.5,
					"recoil": 8,
					"shotEmitter": { "type": "trailing_smoke", "emitProbability": 0.002 }
				} },
				{ "bonuses": [ "DECK_GUNS" ], "value": {
					"back": { "src": "modules", "x": 34, "y": 32 },
					"shot": { "src": "modules", "x": 149, "y": 482, "w": 3, "h": 3 },
					"barrel": { "src": "modules", "x": 320, "y": 823, "w": 50, "h": 10 },
					"barrelX": -2, "barrelY": 4,
					"recoil": 8
				} },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": {
					"back": { "src": "modules", "x": 34, "y": 32 },
					"shot": { "src": "modules", "x": 149, "y": 482, "w": 3, "h": 3 },
					"barrel": { "src": "modules", "x": 503, "y": 768, "w": 46, "h": 8 },
					"barrelX": 2, "barrelY": 5,
					"recoil": 8
				} }
			]
		},
		"fireSound": { "layers": [
			{
				"variations": [ "cannon0", "cannon1", "cannon2", "cannon3", "cannon4", "cannon5", "cannon6" ],
				"volume": {
					"value": 2,
					"distance": [
						0, 1,
						750, 0.75,
						2000, 0.3,
						3000, 0.2,
						4000, 0.1,
						5000, 0
					]
				},
				"pitch": {
					"min": 0.9, "max": 1.2,
					"distance": [
						0, 1,
						2000, 0.9,
						4000, 0.75
					]
				}
			},
			{
				"variations": [ "cannon_high_1", "cannon_high_2", "cannon_high_3", "cannon_high_4", "cannon_high_5", "cannon_high_6" ],
				"volume": {
					"value": 0.3,
					"distance": [
						0, 1,
						750, 0.75,
						2000, 0.3,
						3000, 0.2,
						4000, 0.1,
						5000, 0
					]
				},
				"pitch": {
					"min": 0.9, "max": 1.2,
					"distance": [
						0, 1,
						2000, 0.9,
						4000, 0.75
					]
				}
			},
			{
				"variations": [ "cannon_d_0", "cannon_d_1", "cannon_d_2", "cannon_d_3" ],
				"volume": {
					"value": 0.6,
					"distance": [
						0, 0,
						750, 0,
						2000, 0.1,
						3000, 0.5,
						4000, 0.75,
						5000, 0.1
					]
				},
				"pitch": {
					"min": 0.9, "max": 1.2,
					"distance": [
						0, 1,
						2000, 1,
						5000, 0.85
					]
				}
			} ]
		}
	},
	{
		"name": "FLIPPED_CANNON_WDECK",
		"flippedFrom": "CANNON_WDECK"
	},
	{
		"name": "CANNON_WDECK",
		"categories": ["BASIC", "WEAPONS"],
		"required": "CANNONS",
		"isWeapon": true, "isGun": true, "isCannon": true,
		"sort": 10,
		"w": 2, "h": 1,
		"appearance": {
			"base": { "src": "modules", "x": 40, "y": 3, "w": 2 },
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": { "src": "modules", "x": 40, "y": 7, "w": 2 } },
				{ "bonuses": [ "DECK_GUNS" ], "value": { "src": "modules", "x": 40, "y": 5, "w": 2 } },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": { "src": "modules", "x": 40, "y": 4, "w": 2 } }
			]
		},
		"mask": { "x": 32, "y": 38 },
        "externalAppearances": {
			"base": [],
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": [ {
					"x": 1, "y": 0,
					"appearance": { "src": "modules", "x": 43, "y": 18 }
				} ] },
				{ "bonuses": [ "DECK_GUNS" ], "value": [ {
					"x": 1, "y": 0,
					"appearance": { "src": "modules", "x": 44, "y": 18 }
				} ] }
			]
		},
		"drawExternalsBelowDecals": true,
		"frontOnly": true,
		"moveDelay": 600,
		"hp": 80,
		"fireHP": 50,
        "producesHorizontalDrag": false,
		"explodeHP": { "base": 25, "SAFER_CANNONS": 0 },
		"explodeDmg": { "base": 35, "SAFER_CANNONS": 0 },
		"weight": 65,
		"cost": 75,
		"crew": 1,
		"recommendedCrew": 2, "recommendedGuards": 1,
		"penDmg": { "base": 40, "multipliers": { "INCREASED_CANNON_DAMAGE": 1.2, "MASTER_METALLURGIST": 1.2, "HEAVY_GUNNERY": 1.5 } },
		"reload": { "base": 3500, "multipliers": { "FASTER_CANNON_RELOAD": 0.8, "HEAVY_GUNNERY": 1.3 } },
		"clip": 1,
		"recoilForce": 1.2,
		"inaccuracy": { "base": 0.0014, "PRECISE_GUNNERY": 0.0007 },
		"optimumRange": 400,
		"fireArc": { "direction": "forwards", "degrees": 70 },
		"muzzleCenterX": {
			"base": 1.594,
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": 1.437 },
				{ "bonuses": [ "DECK_GUNS" ], "value": 1.437 },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": 1.562 }
			]
		},
		"muzzleCenterY": {
			"base": 0.531,
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": 0.562 },
				{ "bonuses": [ "DECK_GUNS" ], "value": 0.562 },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": 0.562 }
			]
		},
		"muzzleLength": {
			"base": 0.969,
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": 1.594 },
				{ "bonuses": [ "DECK_GUNS" ], "value": 1.625 },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": 1.5 }
			]
		},
		"hitParticle": "damaged_spark",
		"weaponAppearance": {
			"base": {
				"back": { "src": "modules", "x": 34, "y": 32 },
				"shot": { "src": "modules", "x": 149, "y": 482, "w": 3, "h": 3 },
				"barrel": { "src": "modules", "x": 330, "y": 791, "w": 29, "h": 13 },
				"barrelX": 11,
				"barrelY": 2,
				"recoil": 6
			},
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": {
					"back": { "src": "modules", "x": 27, "y": 51 },
					"shot": { "src": "modules", "x": 155, "y": 488, "w": 4, "h": 2 },
					"barrel": { "src": "modules", "x": 551, "y": 824, "w": 49, "h": 9 },
					"barrelX": -1.5, "barrelY": 4.5,
					"recoil": 8,
					"shotEmitter": { "type": "trailing_smoke", "emitProbability": 0.002 }
				} },
				{ "bonuses": [ "DECK_GUNS" ], "value": {
					"back": { "src": "modules", "x": 34, "y": 32 },
					"shot": { "src": "modules", "x": 149, "y": 482, "w": 3, "h": 3 },
					"barrel": { "src": "modules", "x": 320, "y": 823, "w": 50, "h": 10 },
					"barrelX": -2, "barrelY": 4,
					"recoil": 8
				} },
				{ "bonuses": [ "IMPERIAL_CANNON" ], "value": {
					"back": { "src": "modules", "x": 34, "y": 32 },
					"shot": { "src": "modules", "x": 149, "y": 482, "w": 3, "h": 3 },
					"barrel": { "src": "modules", "x": 503, "y": 768, "w": 46, "h": 8 },
					"barrelX": 2, "barrelY": 5,
					"recoil": 8
				} }
			]
		},
		"fireSound": { "layers": [
			{
				"variations": [ "cannon0", "cannon1", "cannon2", "cannon3", "cannon4", "cannon5", "cannon6" ],
				"volume": {
					"value": 2,
					"distance": [
						0, 1,
						750, 0.75,
						2000, 0.3,
						3000, 0.2,
						4000, 0.1,
						5000, 0
					]
				},
				"pitch": {
					"min": 0.9, "max": 1.2,
					"distance": [
						0, 1,
						2000, 0.9,
						4000, 0.75
					]
				}
			},
			{
				"variations": [ "cannon_high_1", "cannon_high_2", "cannon_high_3", "cannon_high_4", "cannon_high_5", "cannon_high_6" ],
				"volume": {
					"value": 0.3,
					"distance": [
						0, 1,
						750, 0.75,
						2000, 0.3,
						3000, 0.2,
						4000, 0.1,
						5000, 0
					]
				},
				"pitch": {
					"min": 0.9, "max": 1.2,
					"distance": [
						0, 1,
						2000, 0.9,
						4000, 0.75
					]
				}
			},
			{
				"variations": [ "cannon_d_0", "cannon_d_1", "cannon_d_2", "cannon_d_3" ],
				"volume": {
					"value": 0.6,
					"distance": [
						0, 0,
						750, 0,
						2000, 0.1,
						3000, 0.5,
						4000, 0.75,
						5000, 0.1
					]
				},
				"pitch": {
					"min": 0.9, "max": 1.2,
					"distance": [
						0, 1,
						2000, 1,
						5000, 0.85
					]
				}
			} ]
		}
	}
]
"""
imp_cannon = """[
	{
		"name": "FLIPPED_IMP_CANNON",
		"flippedFrom": "IMP_CANNON"
	},
	{
		"name": "IMP_CANNON",
		"categories": ["WEAPONS"], "sort": 16,
		"required": "IMPERIAL_CANNON",
		"isWeapon": true, "isGun": true, "isCannon": true,
		"w": 5, "h": 3,
		"appearance": {
			"base": { "src": "modules", "x": 48, "y": 3, "w": 5, "h": 3 },
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": { "src": "modules", "x": 48, "y": 15, "w": 5, "h": 3 } }
			]
		},
		"canOccupy": [
			{ "x": 0, "y": 2 },
			{ "x": 1, "y": 2 },
			{ "x": 2, "y": 2 },
			{ "x": 3, "y": 2 },
			{ "x": 4, "y": 2 },
			{ "x": 0, "y": 0 },
			{ "x": 0, "y": 1 }
		],
		"upDoors": [ 0 ], "leftDoors": [ 2 ],
		"frontOnly": true,
		"moveDelay": 600,
		"hp": 500,
		"fireHP": 220,
		"explodeHP": { "base": 150, "SAFER_CANNONS": 0 },
		"explodeDmg": { "base": 300, "SAFER_CANNONS": 0 },
		"weight": 400,
		"cost": 700,
		"crew": 4,
		"recommendedCrew": 5, "recommendedGuards": 1,
		"penDmg": { "base": 320, "multipliers": { "INCREASED_CANNON_DAMAGE": 1.2, "MASTER_METALLURGIST": 1.2, "HEAVY_GUNNERY": 1.5 } },
		"reload": { "base": 8000, "multipliers": { "FASTER_CANNON_RELOAD": 0.8, "HEAVY_GUNNERY": 1.3 } },
		"clip": 1, "ammoPerClip": 2,
		"recoilForce": 8.0,
		"shotSpeed": 1.3,
		"inaccuracy": { "base": 0.0018, "PRECISE_GUNNERY": 0.0009 },
		"optimumRange": 400,
		"fireArc": { "direction": "forwards", "degrees": 45 },
		"muzzleCenterX": {
			"base": 3.781,
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": 4.031 }
			]
		},
		"muzzleCenterY": {
			"base": 1.5,
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": 1.406 }
			]
		},
		"muzzleLength": {
			"base": 2.562,
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": 6 }
			]
		},
		"hitParticle": "damaged_spark",
		"weaponAppearance": {
			"base": {
				"back": { "src": "modules", "x": 48, "y": 9, "w": 4, "h": 3 },
				"shot": { "src": "modules", "x": 147, "y": 451, "w": 13, "h": 13 },
				"barrel": { "src": "modules", "x": 768, "y": 192, "w": 80, "h": 24 },
				"barrelX": 20.5, "barrelY": 12,
				"recoil": 18,
				"shotEmitter": { "type": "trailing_smoke", "emitProbability": 0.003 },
				"impactParticle": "rock_bit", "numImpactParticles": 10
			},
			"cases": [
				{ "bonuses": [ "DECK_GUNS", "INCREASED_CANNON_DAMAGE" ], "value": {
					"back": { "src": "modules", "x": 46, "y": 15, "w": 2, "h": 3 },
					"shot": { "src": "modules", "x": 750, "y": 288, "w": 18, "h": 9 },
					"barrel": { "src": "modules", "x": 659, "y": 297, "w": 189, "h": 29 },
					"barrelX": -30, "barrelY": 8,
					"recoil": 24,
					"shotEmitter": { "type": "trailing_smoke", "emitProbability": 0.01 }
				} }
			]
		},
		"fireSound": { "layers": [
			{
				"variations": [ "cannon0", "cannon1", "cannon2", "cannon3", "cannon4", "cannon5", "cannon6" ],
				"volume": {
					"value": 3,
					"distance": [
						0, 1,
						750, 0.75,
						2000, 0.3,
						3000, 0.2,
						4000, 0.1,
						5000, 0
					],
				},
				"pitch": {
					"min": 0.8, "max": 1.1,
					"distance": [
						0, 1,
						2000, 0.9,
						4000, 0.75
					]
				}
			},
			{
				"variations": [ "hv_cannon2" ],
				"volume": {
					"value": 4,
					"distance": [
						0, 1,
						3000, 0.75,
						6000, 0.5,
						8000, 0.2,
						10000, 0.1
					],
				},
				"pitch": {
					"min": 0.8, "max": 1.1,
					"distance": [
						0, 1,
						2000, 0.9,
						4000, 0.75
					]
				}
			},
			{
				"variations": [ "cannon_d_0", "cannon_d_1", "cannon_d_2", "cannon_d_3" ],
				"volume": {
					"value": 2.5,
					"distance": [
						0, 0,
						750, 0,
						2000, 0.1,
						3000, 0.5,
						4000, 0.75,
						5000, 0.1
					],
				},
				"pitch": {
					"min": 0.8, "max": 1.1,
					"distance": [
						0, 1,
						2000, 1,
						5000, 0.85
					]
				}
			}	
		] }
	}
]
"""
