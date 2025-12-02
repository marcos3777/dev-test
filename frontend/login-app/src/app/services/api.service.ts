import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:5000/api';

  constructor(private http: HttpClient) { }

  // TODO: Implementar chamada para login
  login(email: string, password: string): Observable<any> {
    // TODO: O candidato deve implementar esta chamada
    throw new Error('TODO: Implementar chamada de login');
  }

  // TODO: Implementar chamada para cadastro
  register(email: string, password: string): Observable<any> {
    // TODO: O candidato deve implementar esta chamada
    throw new Error('TODO: Implementar chamada de cadastro');
  }

  // Exemplo de chamada implementada - verificar se email existe
  checkEmailExists(email: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/check-email`, { email });
  }
}