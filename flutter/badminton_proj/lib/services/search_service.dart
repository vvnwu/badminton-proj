import 'package:http/http.dart' as http;

class SearchService {
  static Future<String> searchDjangoApi(String query) async {
    String url = 'http://localhost:8000/foods/?search=$query';

    http.Response response = await http.get(Uri.encodeFull(url));

    return response.body;
  }
}
