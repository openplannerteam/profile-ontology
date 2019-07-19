import json

with open('car.jsonld') as f:
	obj = json.load(f)
	for key in ('hasAccessRules', 'hasOnewayRules', 'hasSpeedRules', 'hasPriorityRules', 'hasObstacleRules'):
		rules = obj[key]

		for rule in rules:
			conclusion = {}

			for other_key in ('hasAccess', 'isOneway', 'isReversed', 'hasSpeed', 'hasPriority', 'isObstacle'):
				if other_key in rule:
					conclusion[other_key] = rule.pop(other_key)
			rule['concludes'] = conclusion
			rule['hasOrder'] = rule.pop('hasOrder')
	print(json.dumps(obj, indent=2))