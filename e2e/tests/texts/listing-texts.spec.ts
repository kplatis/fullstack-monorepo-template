import test, { expect } from "@playwright/test";
import { ListingTextsPage } from "../../pages/ListingTripsPage";

test("has title", async ({ page }) => {
  const listingTextsPage = new ListingTextsPage(page);

  await listingTextsPage.goto();

  await expect(page.locator("h1")).toHaveText("Texts");
});

test("has 1 listed items", async ({ page }) => {
  const listingTextsPage = new ListingTextsPage(page);
  await listingTextsPage.goto();

  const cards = await page.getByTestId("text-card").all();
  expect(cards.length).toBe(2);
});

test("clicking on a card redirects the user", async ({ page }) => {
  const listingTextsPage = new ListingTextsPage(page);
  await listingTextsPage.goto();

  await page.waitForSelector('[data-testid="text-card"]');
  const cards = await page.getByTestId("text-card").all();
  const firstCard = cards[0];

  await Promise.all([page.waitForURL("**/texts/*"), firstCard.click()]);

  expect(page.url()).toMatch(
    "http://localhost:3001/texts/8fa1f8bb-6b8e-4b69-923c-1c0a2c32f7e7"
  );
});
