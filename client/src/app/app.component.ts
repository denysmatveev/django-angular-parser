import { Component } from "@angular/core";
import { Http } from "@angular/http";
import { map } from "rxjs/operators";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"],
})
export class AppComponent {
  constructor(private http: Http) {}
  httpdata;
  ngOnInit() {
    this.http
      .get("http://127.0.0.1:8000/api/data/")
      .pipe(map((response) => response.json()))
      .subscribe((data) => this.displaydata(data));
  }
  displaydata(data) {
    this.httpdata = data.data;
  }
}