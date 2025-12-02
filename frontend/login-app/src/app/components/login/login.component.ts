import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';
  isLoading: boolean = false;

  constructor(
    private apiService: ApiService,
    private router: Router
  ) {}

  onSubmit() {
    if (!this.email || !this.password) {
      this.errorMessage = 'Por favor, preencha todos os campos';
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';

    // TODO: Implementar lógica de login
    try {
      this.apiService.login(this.email, this.password).subscribe({
        next: (response) => {
          console.log('Login bem-sucedido', response);
          // TODO: Salvar token/sessão e redirecionar
          this.router.navigate(['/dashboard']);
        },
        error: (error) => {
          this.errorMessage = 'Erro ao fazer login. Verifique suas credenciais.';
          this.isLoading = false;
        }
      });
    } catch (error) {
      this.errorMessage = 'TODO: Implementar chamada de login no ApiService';
      this.isLoading = false;
    }
  }
}