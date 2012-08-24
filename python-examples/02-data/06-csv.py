actors = [
        {
        'name':'Chuck',
        'surname':'Norris',
        'movie':'Firewalker'
    }, {
        'name':'Bruce',
        'surname':'Lee',
        'movie':'For a moment'
    }
]


csv = open('actors.csv','w')
for actor in actors:
    csv.write(actor['name'] + ";" + actor['surname'] + ";" + actor['movie'] + '\n')

csv.close()