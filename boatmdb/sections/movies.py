import requests

from boatmdb.api import TheMovieDBAPI


class Movie(TheMovieDBAPI):

    ADD_URL = {
        'details': '/movie/{id}',
        'account_states': '/movie/{id}/account_states',
        'alternative_titles': '/movie/{id}/alternative_titles',
        'changes': '/movie/{id}/changes',
        'credits': '/movie/{id}/credits',
        'external_ids': '/movie/{id}/external_ids',
        'images': '/movie/{id}/images',
        'keywords': '/movie/{id}/keywords',
        'lists': '/movie/{id}/lists',
        'recommendations': '/movie/{id}/recommendations',
        'release_dates': '/movie/{id}/release_dates',
        'reviews': '/movie/{id}/reviews',
        'similar_movies': '/movie/{id}/similar_movies',
        'translations': '/movie/{id}/translations',
        'videos': '/movie/{id}/videos',
        'watch_providers': '/movie/{id}/watch/providers',
        'rate_movie': '/movie/{id}/rating',
        'delete_rating': '/movie/{id}/rating',
        'latest': '/movie/{id}/latest',
        'now_playing': '/movie/{id}/now_playing',
        'popular': '/movie/{id}/popular',
        'top_rated': '/movie/{id}/top_rated',
        'upcoming': '/movie/{id}/upcoming',
    }

    def get_details(self):
        data = self._call_api(self.ADD_URL['details'].format(id=self.id))
        return data

    def get_account_states(self):
        return

    def get_alternative_titles(self):
        return

    def get_changes(self):
        return

    def get_credits(self):
        return

    def get_external_ids(self):
        return

    def get_images(self):
        return

    def get_keywords(self):
        return

    def get_lists(self):
        return

    def get_recommendations(self):
        return

    def get_release_dates(self):
        return

    def get_reviews(self):
        return

    def get_similar_movies(self):
        return

    def get_translations(self):
        return

    def get_videos(self):
        return

    def get_watch_providers(self):
        return

    def post_rate_movie(self):
        return

    def delete_delete_rating(self):
        return

    def get_latest(self):
        return

    def get_now_playing(self):
        return

    def get_popular(self):
        return

    def get_top_rated(self):
        return

    def get_upcoming(self):
        return

pass