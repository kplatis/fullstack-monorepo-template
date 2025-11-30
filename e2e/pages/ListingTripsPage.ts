import { expect, Page } from "@playwright/test";

export class ListingTextsPage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto("http://localhost:3001/texts");
    await this.page.waitForLoadState("networkidle");
  }

  async expectTitleToContain(substring: string) {
    await expect(this.page).toHaveTitle(substring);
  }
}
