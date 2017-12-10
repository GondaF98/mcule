Clone the following git repository to you computer. The repository contains the skeleton of a Django 1.11.7 project called "mol" using Python2. We created some files already (`mol/models.py`, `mol/admin.py`, `mol/management/commands/load_compounds.py`), you have to write the missing parts only. Feel free to create new files / modify settings if you think it's needed but believe everything is already there for you. You can just use sqlite for the database.

You can find a file called "data" in the root directory. Every line in the data file is a so called "SMILES string" and it describes a "compound". A compound can be a multicomponent one. The componens are separated with dots and the components themselves are compounds as well. Let's call the number of occurences of a component inside a compound "multiplicity".

Some examples:

- the `A.B.B.C.C.C` SMILES string describes a multicomponent compound where the components are `A` with multiplicity 1, `B` with multiplicity 2 and `C` with multiplicity 3. `A`, `B`, and `C` are compounds as well.
- `ABCDEFGH` is a not a multicomponent compound since it doesn't contain dots.
- `A.B.C.C` and `C.A.B.C` are the same compounds because they have the exact same components with the exact same multiplicity.

Write a management command (`mol/management/commands/load_compounds.py`) that iterates over the SMILES string entries (lines in the data file) and load them into the database in the following way:

- Create a compound if it is not in the database yet thus duplicate compounds are not allowed. Use the `Compound` model in `mol/models.py` to store them, you have to write the missing model field definitions.
- If the compound is a multicomponent compound create component relations for the "parent" compound. Use the `ComponentRelation` model in `mol/models.py` and write the missing model field definitions. So for example for the `A.B.B` compound you should create the following relations: parent: `A.B.B`, components: `A` with multiplicity 1, `B` with multiplicity 2.


Example data:
```
A
A.B
A.B.C.C
B.A
A.B.B
C.B.A.C
```

After loading this data the database should contain the following compounds: 
`A`, `B`, `A.B`, `C`, `A.B.C.C`, `A.B.B`

And the following component relations:

- `A.B` - parent: `A.B`, components: `A` with multiplicity 1, `B` with multiplicity 1
- `A.B.C.C` - parent: `A.B.C.C`, components: `A` with multiplicity 1, `B` with multiplicity 1, `C` with multiplicity 2
- `B.A` is the same as `A.B` because it has the exact same components with the exact same multiplicity so it must be skipped
- `A.B.B` - parent: `A.B.B`, components: `A` with multiplicity 1, `B` with multiplicity 2
- `C.A.B.C` is the same as `A.B.C.C` because it has the exact same components with the exact same multiplicity so it must be skipped

Checking whether a multicomponent compound already exists in the database with the exact same components should be done on the database level. It is important that you can't manipulate/normalize the entry strings in a way so that you somehow convert `B.A` to `A.B` before checking and loading it. You have to write a database query using the django ORM to check it. A good place to do it is in a manager class, this is why we prepared the `get_with_same_components` method of the `CompoundManager` class in `mol/models.py` for you.

Bonus task:
Write an API endpoint that returns compounds nested with their components using Django REST framework (http://www.django-rest-framework.org/).
We won't give you detailed instructions on how to do it, we let your imagination fly. :)


After you are done with your work, please zip the whole thing together in a file and send us back. We'll check it asap. 
Thank you!