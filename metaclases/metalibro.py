class MetaLibro(type):
    _isbns = set()

    def __call__(cls, *args, **kwargs):
        if len(args) >= 3:
            isbn = args[2]
        else:
            isbn = kwargs.get('isbn')

        if isbn in cls._isbns:
            raise ValueError(f"El ISBN {isbn} ya esta registrado")

        instance = super().__call__(*args, **kwargs)
        cls._isbns.add(isbn)
        return instance

    @classmethod
    def limpiar_isbns(mcs):
        mcs._isbns.clear()
