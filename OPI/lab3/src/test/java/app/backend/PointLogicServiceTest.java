package app.backend;

import app.backend.service.PointLogicService;
import org.junit.Before;
import org.junit.Test;
import java.math.BigDecimal;
import static org.junit.Assert.*;

public class PointLogicServiceTest {

    private PointLogicService service;

    @Before
    public void setUp() {
        service = new PointLogicService();
    }

    @Test
    public void testCircle_centerIsHit() {
        assertTrue(service.checkHit(
            new BigDecimal("0"), new BigDecimal("0"), new BigDecimal("2")));
    }

    @Test
    public void testCircle_pointInsideIsHit() {
        assertTrue(service.checkHit(
            new BigDecimal("-1"), new BigDecimal("0"), new BigDecimal("2")));
    }

    @Test
    public void testCircle_pointOutsideIsNotHit() {
        assertFalse(service.checkHit(
            new BigDecimal("-2"), new BigDecimal("1"), new BigDecimal("2")));
    }

    @Test
    public void testCircle_pointOnBoundaryIsHit() {
        assertTrue(service.checkHit(
            new BigDecimal("0"), new BigDecimal("1"), new BigDecimal("2")));
    }

    @Test
    public void testRectangle_pointInsideIsHit() {
        assertTrue(service.checkHit(
            new BigDecimal("-1"), new BigDecimal("-1"), new BigDecimal("2")));
    }

    @Test
    public void testRectangle_pointOnCornerIsHit() {
        assertTrue(service.checkHit(
            new BigDecimal("-2"), new BigDecimal("-2"), new BigDecimal("2")));
    }

    @Test
    public void testRectangle_pointOutsideIsNotHit() {
        assertFalse(service.checkHit(
            new BigDecimal("-3"), new BigDecimal("-1"), new BigDecimal("2")));
    }

    @Test
    public void testRectangle_pointBeyondYIsNotHit() {
        assertFalse(service.checkHit(
            new BigDecimal("-1"), new BigDecimal("-3"), new BigDecimal("2")));
    }

    @Test
    public void testTriangle_pointInsideIsHit() {
        assertTrue(service.checkHit(
            new BigDecimal("0"), new BigDecimal("0"), new BigDecimal("2")));
    }

    @Test
    public void testTriangle_pointAtApexIsHit() {
        assertTrue(service.checkHit(
            new BigDecimal("0"), new BigDecimal("1"), new BigDecimal("2")));
    }

    @Test
    public void testTriangle_pointOutsideIsNotHit() {
        assertFalse(service.checkHit(
            new BigDecimal("1"), new BigDecimal("1"), new BigDecimal("2")));
    }

    @Test
    public void testTriangle_pointBeyondRIsNotHit() {
        assertFalse(service.checkHit(
            new BigDecimal("3"), new BigDecimal("0"), new BigDecimal("2")));
    }

    @Test
    public void testFourthQuadrant_alwaysMiss() {
        assertFalse(service.checkHit(
            new BigDecimal("1"), new BigDecimal("-1"), new BigDecimal("2")));
    }

    @Test
    public void testFourthQuadrant_closeToOriginIsMiss() {
        assertFalse(service.checkHit(
            new BigDecimal("0.1"), new BigDecimal("-0.1"), new BigDecimal("3")));
    }

    @Test
    public void testWithR1_rectangleHit() {
        assertTrue(service.checkHit(
            new BigDecimal("-0.5"), new BigDecimal("-0.5"), new BigDecimal("1")));
    }

    @Test
    public void testWithR3_circleHit() {
        assertTrue(service.checkHit(
            new BigDecimal("-1"), new BigDecimal("0"), new BigDecimal("3")));
    }
}