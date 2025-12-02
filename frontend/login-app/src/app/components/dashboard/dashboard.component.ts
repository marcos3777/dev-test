import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div style="max-width: 800px; margin: 50px auto; padding: 20px;">
      <h1>Dashboard</h1>
      <p>Parabéns! Você está logado no sistema.</p>
      <button (click)="logout()" style="padding: 10px 20px; background-color: #dc3545; color: white; border: none; cursor: pointer;">
        Sair
      </button>
    </div>
  `,
  styles: []
})
export class DashboardComponent {
  constructor(private router: Router) {}

  logout() {
    // TODO: Limpar sessão/token
    this.router.navigate(['/login']);
  }
}