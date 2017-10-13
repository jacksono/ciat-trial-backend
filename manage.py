"""Migrations script to handle changes in data models."""

from inm.app import db, app
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand
from inm.models import Observation # noqa
from xlrd import open_workbook

# Manager instance
manager = Manager(app)

# Set up migrate commands
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def initdb():
    """Create all tables."""
    db.create_all()
    print('Initialised the database')


@manager.command
def dropdb():
    """Clear all the data in the tables."""
    if prompt_bool("Are you sure you want to loose all your data?"):
        db.drop_all()
        print("Dropped the database")


@manager.command
def populatedb():
    """Populate all the data in the tables."""
    if prompt_bool("Are you sure you want to add the data?"):
        wb = open_workbook("sample.xlsx")
        sheet = wb.sheets()[0]
        for row in range(1, sheet.nrows):
            obj = Observation(plot_num=sheet.row(row)[0].value,
                              combination={'FYM': sheet.row(row)[3].value,
                                           'ROTATION': sheet.row(row)[4].value,
                                           'RESIDUES': sheet.row(row)[6].value,
                                           'N': sheet.row(row)[2].value,
                                           'P': sheet.row(row)[7].value[(sheet.row(row)[7].value.index('_') + 1):],
                                           'REP': sheet.row(row)[1].value},
                              _2004={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[13].value, sheet.row(row)[8].value],
                                     'Maize_AGB': [sheet.row(row)[14].value, sheet.row(row)[9].value],
                                     'Teph_AGB': [sheet.row(row)[15].value, sheet.row(row)[10].value],
                                     'Soy_Y': [sheet.row(row)[16].value, sheet.row(row)[11].value],
                                     'Soy_AGB': [sheet.row(row)[17].value,
                                                 sheet.row(row)[12].value]},
                              _2005={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[23].value, sheet.row(row)[18].value],
                                     'Maize_AGB': [sheet.row(row)[24].value, sheet.row(row)[19].value],
                                     'Teph_AGB': [sheet.row(row)[25].value, sheet.row(row)[20].value],
                                     'Soy_Y': [sheet.row(row)[26].value, sheet.row(row)[21].value],
                                     'Soy_AGB': [sheet.row(row)[27].value,
                                                 sheet.row(row)[22].value]},
                              _2006={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[33].value, sheet.row(row)[28].value],
                                     'Maize_AGB': [sheet.row(row)[34].value, sheet.row(row)[29].value],
                                     'Teph_AGB': [sheet.row(row)[35].value, sheet.row(row)[30].value],
                                     'Soy_Y': [sheet.row(row)[36].value, sheet.row(row)[31].value],
                                     'Soy_AGB': [sheet.row(row)[37].value,
                                                 sheet.row(row)[32].value]},
                              _2007={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[43].value, sheet.row(row)[38].value],
                                     'Maize_AGB': [sheet.row(row)[44].value, sheet.row(row)[39].value],
                                     'Teph_AGB': [sheet.row(row)[45].value, sheet.row(row)[40].value],
                                     'Soy_Y': [sheet.row(row)[46].value, sheet.row(row)[41].value],
                                     'Soy_AGB': [sheet.row(row)[47].value,
                                                 sheet.row(row)[42].value]},
                              _2008={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[53].value, sheet.row(row)[48].value],
                                     'Maize_AGB': [sheet.row(row)[54].value, sheet.row(row)[49].value],
                                     'Teph_AGB': [sheet.row(row)[55].value, sheet.row(row)[50].value],
                                     'Soy_Y': [sheet.row(row)[56].value, sheet.row(row)[51].value],
                                     'Soy_AGB': [sheet.row(row)[57].value,
                                                 sheet.row(row)[52].value]},
                              _2009={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[63].value, sheet.row(row)[58].value],
                                     'Maize_AGB': [sheet.row(row)[64].value, sheet.row(row)[59].value],
                                     'Teph_AGB': [sheet.row(row)[65].value, sheet.row(row)[60].value],
                                     'Soy_Y': [sheet.row(row)[66].value, sheet.row(row)[61].value],
                                     'Soy_AGB': [sheet.row(row)[67].value,
                                                 sheet.row(row)[62].value]},
                              _2010={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[73].value, sheet.row(row)[68].value],
                                     'Maize_AGB': [sheet.row(row)[74].value, sheet.row(row)[69].value],
                                     'Teph_AGB': [sheet.row(row)[75].value, sheet.row(row)[70].value],
                                     'Soy_Y': [sheet.row(row)[76].value, sheet.row(row)[71].value],
                                     'Soy_AGB': [sheet.row(row)[77].value,
                                                 sheet.row(row)[72].value]},
                              _2011={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[83].value, sheet.row(row)[78].value],
                                     'Maize_AGB': [sheet.row(row)[84].value, sheet.row(row)[79].value],
                                     'Teph_AGB': [sheet.row(row)[85].value, sheet.row(row)[80].value],
                                     'Soy_Y': [sheet.row(row)[86].value, sheet.row(row)[81].value],
                                     'Soy_AGB': [sheet.row(row)[87].value,
                                                 sheet.row(row)[82].value]},
                              _2012={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[93].value, sheet.row(row)[88].value],
                                     'Maize_AGB': [sheet.row(row)[94].value, sheet.row(row)[89].value],
                                     'Teph_AGB': [sheet.row(row)[95].value, sheet.row(row)[90].value],
                                     'Soy_Y': [sheet.row(row)[96].value, sheet.row(row)[91].value],
                                     'Soy_AGB': [sheet.row(row)[97].value,
                                                 sheet.row(row)[92].value]},
                              _2013={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[103].value, sheet.row(row)[98].value],
                                     'Maize_AGB': [sheet.row(row)[104].value, sheet.row(row)[99].value],
                                     'Teph_AGB': [sheet.row(row)[105].value, sheet.row(row)[100].value],
                                     'Soy_Y': [sheet.row(row)[106].value, sheet.row(row)[101].value],
                                     'Soy_AGB': [sheet.row(row)[107].value,
                                                 sheet.row(row)[102].value]},
                              _2014={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[113].value, sheet.row(row)[108].value],
                                     'Maize_AGB': [sheet.row(row)[114].value, sheet.row(row)[109].value],
                                     'Teph_AGB': [sheet.row(row)[115].value, sheet.row(row)[110].value],
                                     'Soy_Y': [sheet.row(row)[116].value, sheet.row(row)[111].value],
                                     'Soy_AGB': [sheet.row(row)[117].value,
                                                 sheet.row(row)[112].value]},
                              _2015={'plot': sheet.row(row)[0].value,
                                     'Maize_Y': [sheet.row(row)[123].value, sheet.row(row)[118].value],
                                     'Maize_AGB': [sheet.row(row)[124].value, sheet.row(row)[119].value],
                                     'Teph_AGB': [sheet.row(row)[125].value, sheet.row(row)[120].value],
                                     'Soy_Y': [sheet.row(row)[126].value, sheet.row(row)[121].value],
                                     'Soy_AGB': [sheet.row(row)[127].value,
                                                 sheet.row(row)[122].value]})

            db.session.add(obj)
            db.session.commit()
            obj = ''

        print("Database Populated")


@manager.command
def migratedb():
    """Migrates the DB."""
    if prompt_bool("Are you sure you want to lmigrate all data"):
        dropdb()
        initdb()
        populatedb()
        print("Database Migrated")


if __name__ == "__main__":
    manager.run()
