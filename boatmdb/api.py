from dataclasses import dataclass
import requests


API_KEY = '022b59c80687e45e884ad950d0134a4d'
movie_id = 666
id = 3


@dataclass
class TheMovieDBAPI:

    id: int
    api_key: str
    api_version: int = 3

    @property
    def base_url(self):
        return f'https://api.themoviedb.org/{self.api_version}'
        # return f'https://api.themoviedb.org/{self.api_version}/movie/{self.id}'

    def _call_api(self, path, in_params=None):
        params = {'api_key': self.api_key}
        params.update(in_params)
        res = requests.get(self.base_url + path, params=params)

        res.raise_for_status()
        return res.json()




# a = TheMovieDBAPI(id=movie_id, api_key=API_KEY).get()

pass
