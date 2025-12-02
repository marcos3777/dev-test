import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {
  email: string = '';
  password: string = '';
  confirmPassword: string = '';
  errorMessage: string = '';
  successMessage: string = '';
  isLoading: boolean = false;

  constructor(
    private apiService: ApiService,
    private router: Router
  ) {}

  async onSubmit() {
    // Validações básicas
    if (!this.email || !this.password || !this.confirmPassword) {
      this.errorMessage = 'Por favor, preencha todos os campos';
      return;
    }

    if (this.password !== this.confirmPassword) {
      this.errorMessage = 'As senhas não coincidem';
      return;
    }

    if (this.password.length < 6) {
      this.errorMessage = 'A senha deve ter pelo menos 6 caracteres';
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';

    // Verificar se email já existe
    this.apiService.checkEmailExists(this.email).subscribe({
      next: (response) => {
        if (response.exists) {
          this.errorMessage = 'Este email já está cadastrado';
          this.isLoading = false;
        } else {
          // TODO: Implementar cadastro
          try {
            this.apiService.register(this.email, this.password).subscribe({
              next: (response) => {
                this.successMessage = 'Cadastro realizado com sucesso!';
                setTimeout(() => {
                  this.router.navigate(['/login']);
                }, 2000);
              },
              error: (error) => {
                this.errorMessage = 'Erro ao realizar cadastro';
                this.isLoading = false;
              }
            });
          } catch (error) {
            this.errorMessage = 'TODO: Implementar chamada de cadastro no ApiService';
            this.isLoading = false;
          }
        }
      },
      error: (error) => {
        this.errorMessage = 'Erro ao verificar email';
        this.isLoading = false;
      }
    });
  }
}